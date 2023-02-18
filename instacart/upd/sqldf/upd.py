from pandas.io.sql import read_sql
from sqlalchemy import text
from sqlalchemy.exc import DatabaseError, ResourceClosedError

from pandasql import PandaSQL
from pandasql.sqldf import get_outer_frame_variables, extract_table_names, write_table, PandaSQLException


class PandaSQLUpdate(PandaSQL):

    def __call__(self, query, env=None):
        if env is None:
            env = get_outer_frame_variables()

        with self.conn as conn:
            for table_name in extract_table_names(query):
                if table_name not in env:
                    continue
                if self.persist and table_name in self.loaded_tables:
                    continue
                self.loaded_tables.add(table_name)
                write_table(env[table_name], table_name, conn)

            try:
                result = read_sql(text(query), conn)
            except DatabaseError as ex:
                raise PandaSQLException(ex)
            except ResourceClosedError:
                result = None

        return result


def sqldf(query, env=None, db_uri='sqlite:///:memory:'):
    return PandaSQLUpdate(db_uri)(query, env)
