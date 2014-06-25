import bottle
from bottle import route, run, post, request, auth_basic, abort
import subprocess, os

bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024 # (or whatever you want)

##################################iems_workshop#############################################
@route('/iems_test_R/') 
def iems_test_R():
    src1="Rscript.exe sobol_example.R"
    subprocess.Popen(src1, shell=0)
    print('done')
##################################iems_workshop#############################################

run(host='localhost', port=80, debug=True)

#Next Step: Go to your browser and 
#visit the following address: http://localhost:80/iems_test_R/


