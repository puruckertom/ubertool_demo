import bottle
from bottle import route, run, post, request, auth_basic, abort
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.bucket import Bucket
import os
import json


bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024 # (or whatever you want)

class NumPyArangeEncoder(json.JSONEncoder):
    def default(self, obj):
        import numpy as np
        if isinstance(obj, np.ndarray):
            return obj.tolist() # or map(int, obj)
        return json.JSONEncoder.default(self, obj)

import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client.ubertool

all_result = {}


##################################terrplant#############################################
@route('/terrplant/<jid>', method='POST') 

def terrplant_rest(jid):
    for k, v in request.json.iteritems():
        exec '%s = v' % k
        # print k, v
    all_result.setdefault(jid,{}).setdefault('status','none')

    from terrplant_rest import terrplant_model_rest
    result = terrplant_model_rest.terrplant(version_terrplant,run_type,A,I,R,D,nms,lms,nds,lds,chemical_name,pc_code,use,application_method,application_form,solubility)
    if (result):
        all_result[jid]['status']='done'
        all_result[jid]['input']=request.json
        all_result[jid]['result']=result

    return {'user_id':'admin', 'result': result.__dict__, '_id':jid}
##################################terrplant#############################################


##################################trex2#############################################
@route('/trex2/<jid>', method='POST') 

def trex2_rest(jid):
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')
    from trex2_rest import trex2_model_rest
    result = trex2_model_rest.trex2(chem_name, use, formu_name, a_i, Application_type, seed_treatment_formulation_name, seed_crop, seed_crop_v, r_s, b_w, p_i, den, h_l, n_a, ar_lb, day_out,
                                    ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird_sm, aw_bird_md, aw_bird_lg, 
                                    Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL, 
                                    tw_bird_ld50, tw_bird_lc50, tw_bird_NOAEC, tw_bird_NOAEL, x, ld50_mamm, lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm_sm, aw_mamm_md, aw_mamm_lg, tw_mamm,
                                    m_s_r_p)
    if (result):
        result_json = json.dumps(result.__dict__, cls=NumPyArangeEncoder)
        all_result[jid]['status']='done'
        all_result[jid]['input']=request.json
        all_result[jid]['result']=result
    return {'user_id':'admin', 'result':result_json, '_id':jid}
##################################trex2#############################################


##################################agdrift#############################################
@route('/agdrift/<jid>', method='POST') 

def agdrift_rest(jid):
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')
    from agdrift_rest import agdrift_model_rest
    result = agdrift_model_rest.agdrift(drop_size, ecosystem_type, application_method, boom_height, orchard_type, application_rate, distance, aquatic_type, calculation_input, init_avg_dep_foa, avg_depo_gha, avg_depo_lbac, deposition_ngL, deposition_mgcm, nasae, y, x, express_y)
    if (result):
        all_result[jid]['status']='done'
        all_result[jid]['input']=request.json
        all_result[jid]['result']=result
    return {'user_id':'admin', 'result': result.__dict__, '_id':jid}
##################################agdrift#############################################


##################################geneec#############################################
@route('/geneec/<jid>', method='POST') 

def geneec_rest(jid):
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')
    from geneec_rest import gfix
    # print request.json
    result = gfix.geneec2(APPRAT,APPNUM,APSPAC,KOC,METHAF,WETTED,METHOD,AIRFLG,YLOCEN,GRNFLG,GRSIZE,ORCFLG,INCORP,SOL,METHAP,HYDHAP,FOTHAP)

    # if (result):
    all_result[jid]['status']='done'
    all_result[jid]['input']=request.json
    all_result[jid]['result']=result

    return {'user_id':'admin', 'result': result, '_id':jid}
##################################geneec#############################################




##########insert results into mongodb#########################
@route('/save_history', method='POST') 

def insert_output_html():
    for k, v in request.json.iteritems():
        exec "%s = v" % k
    element={"user_id":"admin", "_id":_id, "run_type":run_type, "output_html": output_html, "model_object_dict":model_object_dict}
    db[model_name].save(element)
    print _id

@route('/update_html', method='POST') 

def update_output_html():
    for k, v in request.json.iteritems():
        exec "%s = v" % k
    # print request.json
    db[model_name].update({"_id" :_id}, {'$set': {"output_html": output_html}})




###############Check History####################
@route('/user_history', method='POST')

def get_user_model_hist():
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    hist_all = []
    entity = db[model_name].find({'user_id':user_id}).sort("_id", 1)
    for i in entity:
        hist_all.append(i)
    if not entity:
        abort(404, 'No document with jid %s' % jid)
    return {"hist_all":hist_all}

@route('/get_html_output', method='POST')

def get_html_output():
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    html_output_c = db[model_name].find({"_id" :jid}, {"output_html":1, "_id":0})
    for i in html_output_c:
        # print i
        html_output = i['output_html']
    return {"html_output":html_output}

@route('/get_pdf', method='POST')

def get_pdf():
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    final_str = pdf_t
    final_str = final_str + """<br>"""
    if (int(pdf_nop)>0):
        for i in range(int(pdf_nop)):
            final_str = final_str + """<img id="imgChart1" src="%s" />"""%(pdf_p[i])
            final_str = final_str + """<br>"""

    from generate_doc import generatepdf_pi
    result=generatepdf_pi.generatepdf_pi(final_str)
    return {"result":result}

@route('/get_html', method='POST')

def get_html():
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    final_str = pdf_t
    final_str = final_str + """<br>"""
    if (int(pdf_nop)>0):
        for i in range(int(pdf_nop)):
            final_str = final_str + """<img id="imgChart1" src="%s" />"""%(pdf_p[i])
            final_str = final_str + """<br>"""

    from generate_doc import generatehtml_pi
    result=generatehtml_pi.generatehtml_pi(final_str)
    return {"result":result}


run(host='localhost', port=80, debug=True)