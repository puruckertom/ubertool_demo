www.ubertool.com Demo Code from iEMSs 2014 "Scientific Computing in the Cloud" workshop
=============

The demo code for the ubertool contains a Python Google App Engine (GAE) project to demonstrate the cloud-based, cross-platform risk assessment modeling framework.<br>

Included in the demo are examples of different modeling applications such as a Python model (TerrPlant), linked/coupled models (AgDrift / Trex), a FORTRAN model (Geneec), and an example of visual mapping tools.


Dependencies
=============

<a href="https://www.python.org/download/releases/2.7/#download">Python 2.7</a><br>
<a href="https://developers.google.com/appengine/downloads">Google App Engine (Python)</a><br>
<a href="http://www.mongodb.org/downloads">MongoDB</a><br>
<a href="https://pypi.python.org/pypi/pymongo/#downloads">pymongo 2.7.1</a><br>
<a href="https://github.com/boto/boto">boto (Amazon S3 interface)</a><br>


Installation
=============

Clone ubertool_demo repo<br>
If using GAE GUI, add the ubertool_demo directory as an "Existing Application" (File > Add Existing Application).  Once added, click "Run" to start the dev server.<br>
Command line: https://developers.google.com/appengine/docs/python/tools/devserver<br>
<br>
<b>Note:</b> In the iEMSs workshop we had you utilize a VirtulBox VM image (Ubuntu) to the run the development server.  This approach was intended to overcome the installation of dependencies.  The VirtualBox VM is <b>not needed</b> (nor recommended) for exploring the ubertool_demo code and no support is provided for its use.


Using the Development Server
=============

The local dev server requires 3 local servers to be running: MongoDB, Bottle, and GAE<br>

<b>MongoDB:</b> mongod --dbpath C:\Path\to\db <a href="http://docs.mongodb.org/manual/tutorial/getting-started/">MongoDB Help</a><br>

<b>Bottle:</b> python bottle_local.py (The Bottle server is included in the repo "\\REST\\rest_local\\bottle_local.py")<br>
Note: The bottle server requires MongoDB to be running before it will successfully start<br>

<b>GAE:</b> After starting the dev servers, go to localhost:8080 (or whichever port you chose) in your browser.  If using the GAE GUI, click "Browse".<br>


Contact Info
=============

Questions regarding the use of the ubertool_demo code can be directed to Tom Purucker: purucker.tom@gmail.com
