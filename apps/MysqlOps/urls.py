from django.conf.urls import url

# from .views import article_add,upload_image,article_edit,article_index
from roeops.settings import MEDIA_ROOT
from django.views.static import serve
from  MysqlOps.views import  binlog_parse,fast_sql
from MysqlOps.views.fast_sql_api import MyfastSQLAPI
from MysqlOps.views.binlog_parse_api import BinlogRedoAPI,BinlogUndoAPI

urlpatterns = [
    url(r'^binlog_parse/$', binlog_parse.binlog_parse,name='mysql_binglog_parse'),
    url(r'^binlog_redo_api/$', BinlogRedoAPI.as_view(), name='mysql_binglog_redo_api'),
    url(r'^binlog_undo_api/$', BinlogUndoAPI.as_view(), name='mysql_binglog_undo_api'),
    url(r'^mysql_fast_SQL_list/$', fast_sql.MyfastSQL_list,name='mysql_fast_sql_list'),

    url(r'^mysql_fast_SQL_add/$', fast_sql.MyfastSQL_add, name='mysql_fast_sql_add'),
    url(r'^mysql_fast_SQL_edit/$', fast_sql.MyfastSQL_edit, name='mysql_fast_sql_edit'),
    url(r'^mysql_fast_sal_api/$',MyfastSQLAPI.as_view(),name='mysql_fast_sql_api'),

    url(r'^mysql_fast_sql_show/$',fast_sql.MyfastSQL_show,name='mysql_fast_sql_show'),
    # url(r'^mysql_fast_sql_show/$', fast_sql.MyfastSQL_show, name='mysql_fast_sql_show'),
    url(r'^mysql_fast_sql_result/(?P<id>[0-9]+)/$',fast_sql.MyfastSQL_result,name='mysql_fast_sql_result')

 ]