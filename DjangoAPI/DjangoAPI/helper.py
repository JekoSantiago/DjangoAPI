from django.db import connection, connections


def query_db(db, query, args=(), one=False):
    cur = connections[db].cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) 
        for i, value in enumerate(row)) for row in cur.fetchall()]
    # cur.connection.close()
    return (r[0] if r else None) if one else r