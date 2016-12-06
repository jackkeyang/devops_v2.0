#!/usr/bin/env python
#coding:utf-8

from DBUtils.PooledDB import PooledDB
from app import app
import MySQLdb as mysql

class DB():
    def __init__(self):
        self.host = app.config.get("DB_HOST")
        self.user = app.config.get("DB_USER")
        self.passwd = app.config.get("DB_PASSWD")
        self.dbname = app.config.get("DB_NAME")
        self.max_pool = app.config.get("DB_POOL_MAX")
        self.min_pool = app.config.get("DB_POOL_MIN")
        self.pool = PooledDB(
            mysql,
            maxcached = self.max_pool,
            mincached = self.min_pool,
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            db = self.dbname,
            setsession = ['SET AUTOCOMMIT = 1'],
            charset = "utf8"
        )

    def connect_db(self):
        self.db = self.pool.connection()
        self.cur = self.db.cursor()

    def close_db(self):
        self.cur.close()
        self.db.close()

    def execute(self,sql):
        self.connect_db()
        self.cur.execute(sql)

    def get_list(self,table,fields,where=None):
        '''
        table:表名
        fields：查询列,["id","username","password"]
        return : [{'username':'xxx','password':'123'},{xxxxxx},{}]
        '''
        if isinstance(where,dict) and where:
            conditions = []
            for k,v in where.items():
                if isinstance(v, list):
                    conditions.append("%s IN (%s)" % (k, ','.join(v)))
                elif isinstance(v, str) or isinstance(v, unicode):
                    conditions.append("%s='%s'" % (k, v))
                elif isinstance(v, int):
                    conditions.append("%s=%s" % (k, v))
            sql = "select %s from %s where %s" % (",".join(fields),table,' AND '.join(conditions))
        elif not where:
            sql = "select %s from %s"%(",".join(fields),table)
        try:
            self.execute(sql)
            result = self.cur.fetchall()
            if result:
                result = [ dict((v,row[i]) for i,v in enumerate(fields)) for row in result]
            else:
                result = {}
            return result
        except Exception,e:
            print "error",e
        finally:
            self.close_db()

    def get_one(self,table,fields,where):
        '''
        :param table: 表名
        :param fields: 查询列, ["id","name","password"...]
        :param where: 过滤条件, {"id":1}
        :return:{'username': u'admin', 'password': u'123456', 'id': 1L}
        '''
        if isinstance(where,dict):
            where = ["%s='%s'"%(k,v) for k,v in where.items()]
        sql = "select %s from %s where %s"%(",".join(fields),table," and ".join(where))
        try:
            self.execute(sql)
            result = self.cur.fetchone()
            if result:
                result = dict((v,result[i]) for i,v in enumerate(fields))
            else:
                result = {}
            return result
        except Exception,e:
            print e
        finally:
            self.close_db()

    def create(self,table,fields):
        '''
        :param table: 表名
        :param fields: 插入数据库的数据，字典类型{"username":"jack","password":"123"}
        '''
        sql = "insert into %s(%s)values('%s')"%(table,",".join(fields.keys()),"','".join(fields.values()))
        try:
            return self.execute(sql)
        except Exception,e:
            print e
        finally:
            self.close_db()

    def delete(self,table,where):
        '''
        :param table: 表名
        :param where: 删除条件，字典类型 {"username":"jack"}
        '''
        if isinstance(where,dict):
            where = ["%s='%s'"%(k,v) for k,v in where.items()]
        sql = "delete from %s where %s"%(table," and ".join(where))
        try:
            return self.execute(sql)
        except Exception,e:
            print e
        finally:
            self.close_db()

    def update(self,table,fields):
        '''
        :param table:表名
        :param fields: 需要修改的数据，字典类型
        '''
        data = ",".join(["%s='%s'"%(k,v) for k,v in fields.items()])
        sql = "update %s set %s where id=%s"%(table,data,fields["id"])
        try:
            return self.execute(sql)
        except Exception,e:
            print e
            print sql
        finally:
            self.close_db()

if __name__ == "__main__":
    db = DB()
    #print db.get_list("user",["id","username","password"])
    #print db.get_one("user",["id","username","password"],{"id":1})
    #db.create("user",{"username":"jack","password":"123"})
    #db.delete("user",{"username":"jack"})
    db.update("user",{"id":1,"username":"admin"})