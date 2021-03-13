import flask
from flask import request
import json
import math
import statistics

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Home page"

@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page",404

@app.route('/area/square',methods=['GET'])
def square():
    if('s' in request.args):
        s = request.args['s']
        ret = {"a":str(int(s)*int(s)), "s":s}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/area/rectangle',methods=['GET'])
def rectangle():
    if('l' in request.args and 'w' in request.args):
        l = int(request.args['l'])
        w = int(request.args['w'])
        ret = {"a": str(l*w),"l":str(l),"w":str(w)}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/area/triangle',methods=['GET'])
def triangle():
    if('b' in request.args and 'h' in request.args):
        b = int(request.args['b'])
        h = int(request.args['h'])
        ret = {"a": str(b*h/2),"b":str(b),"h":str(h)}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/area/heron',methods=['GET'])
def heron():
    if('a' in request.args and 'b' in request.args and 'c' in request.args):
        b = int(request.args['b'])
        a = int(request.args['a'])
        c = int(request.args['c'])
        s = a+b+c
        area = math.sqrt(s* (s-a) * (s-b) * (s-c))
        ret = {"area":area, "s":s, "a":a, "b":b, "c":c}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/area/parallelogram',methods=['GET'])
def parallelogram():
    if('b' in request.args and 'h' in request.args):
        b = int(request.args['b'])
        h = int(request.args['h'])
        ret = {"a": str(b*h),"b":str(b),"h":str(h)}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/area/circle',methods=['GET'])
def circle():
    if('r' in request.args):
        r = float(request.args['r'])
        ret = {"a":math.pi*r*r, "r":r}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/area/trapezoid',methods=['GET'])
def trapezoid():
    if('b1' in request.args and 'b2' in request.args and 'h' in request.args):
        b1 = int(request.args['b1'])
        b2 = int(request.args['b2'])
        h = int(request.args['h'])
        area = (b1+b2)*h*(1/2)
        ret = {"area":area, "b1":b1, "b2":b2, "h":h}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/surface/cube',methods=['GET'])
def cube():
    if('s' in request.args):
        s = int(request.args['s'])
        ret = {"sa":6*s*s,"s":s}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/surface/sphere',methods=['GET'])
def sphere():
    if('r' in request.args):
        r = float(request.args['r'])
        ret = {"sa":4.0*math.pi*r*r, "r":r}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/surface/cylinder',methods=['GET'])
def cylinder():
    if('r' in request.args and 'h' in request.args):
        r = float(request.args['r'])
        h = float(request.args['h'])
        ret = {"sa":2.0*math.pi*h*r, "r":r,"h":h}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/perimeter/square',methods=['GET'])
def squareP():
    if('s' in request.args):
        s = int(request.args['s'])
        ret = {"p":4*s,"s":s}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/perimeter/rectangle',methods=['GET'])
def rectangleP():
    if('l' in request.args and 'w' in request.args):
        l = int(request.args['l'])
        w = int(request.args['w'])
        ret = {"p": (2*l) + (2*w),"l":str(l),"w":str(w)}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/perimeter/triangle',methods=['GET'])
def triangleP():
    if('s1' in request.args and 's2' in request.args and 's3' in request.args):
        s1 = int(request.args['s1'])
        s2 = int(request.args['s2'])
        s3 = int(request.args['s3'])
        ret = {"p":s1+s2+s3, "s1":s1, "s2":s2, "s3":s3}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/perimeter/circle',methods=['GET'])
def circleP():
    if('d' in request.args):
        d = float(request.args['d'])
        ret = {"p":math.pi*d,"d":d}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/volume/cube',methods=['GET'])
def cubeV():
    if('s' in request.args):
        s = int(request.args['s'])
        ret = {"v":s*s*s,"s":s}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/volume/prism',methods=['GET'])
def prsim():
    if('l' in request.args and 'w' in request.args and 'h' in request.args):
        l = int(request.args['l'])
        w = int(request.args['w'])
        h = int(request.args['h'])
        ret = {"v": l*h*w,"l":str(l),"w":str(w),"h":h}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/volume/pyramid',methods=['GET'])
def pyramid():
    if('b' in request.args and 'h' in request.args):
        b = int(request.args['b'])
        h = int(request.args['h'])
        ret = {"v": b*b*h*(1/3),"b":str(b),"h":h}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/volume/cylinder',methods=['GET'])
def cylinderV():
    if('r' in request.args and 'h' in request.args):
        r = float(request.args['r'])
        h = float(request.args['h'])
        ret = {"v": math.pi*r*r*h,"r":str(r),"h":h}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/volume/cone',methods=['GET'])
def coneV():
    if('r' in request.args and 'h' in request.args):
        r = float(request.args['r'])
        h = float(request.args['h'])
        ret = {"v": math.pi*r*r*h*(1/3),"r":str(r),"h":h}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/volume/sphere',methods=['GET'])
def sphereV():
    if('r' in request.args):
        r = float(request.args['r'])
        ret = {"v": math.pi*r*r*r*(4/3),"r":str(r)}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/distance',methods=['GET'])
def distance():
    if('x1' in request.args and 'x2' in request.args and 'y1' in request.args and 'y2' in request.args):
        x1 = int(request.args['x1'])
        x2 = int(request.args['x2'])
        y1 = int(request.args['y1'])
        y2 = int(request.args['y2'])
        dist = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
        ret = {"dist": dist, "x1":x1,"x2": x1,"y1": x1,"y2":x1}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/slope',methods=['GET'])
def slope():
    if('x1' in request.args and 'x2' in request.args and 'y1' in request.args and 'y1' in request.args):
        x1 = int(request.args['x1'])
        x2 = int(request.args['x2'])
        y1 = int(request.args['y1'])
        y2 = int(request.args['y2'])
        slope = (y2-y1)/(x2-x1)
        ret = {"slope": slope, "x1":x1,"x2": x1,"y1": x1,"y2":x1}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route('/pythag',methods=['GET'])
def pythag():
    args = request.args
    if(len(args)==2):
        if('a' in request.args and 'b' in request.args):
            b = int(request.args['b'])
            a = int(request.args['a'])
            c = math.sqrt((a*a) + (b*b))
            ret = {"a":a, "b":b, "c":c}
            return json.dumps(ret), 200, {"Content-Type":'application/json'}
        elif('a' in request.args and 'c' in request.args):
            c = int(request.args['c'])
            a = int(request.args['a'])
            b = math.sqrt((c*c) - (a*a))
            ret = {"a":a, "b":b, "c":c}
            return json.dumps(ret), 200, {"Content-Type":'application/json'}
        elif('b' in request.args and 'c' in request.args):
            c = int(request.args['c'])
            b = int(request.args['b'])
            a = math.sqrt((c*c) - (b*b))
            ret = {"a":a, "b":b, "c":c}
            return json.dumps(ret), 200, {"Content-Type":'application/json'}
        else:
            return "missing parameters",400
    return "missing parameters",400

@app.route("/mean",methods=["GET"])
def mean():
    if("nums" in request.args):
        nums = []
        sum = 0
        str1 = request.args['nums']
        for x in str1.split(','):
            nums.append(int(x))
            sum+=int(x)
        ret = {"mean": sum/(len(nums)), "nums":nums}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route("/median",methods=["GET"])
def median():
    if("nums" in request.args):
        nums = []
        str1 = request.args['nums']
        for x in str1.split(','):
            nums.append(int(x))
        median = statistics.median(nums)
        ret = {"median": median, "nums":nums}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400

@app.route("/mode",methods=["GET"])
def mode():
    if("nums" in request.args):
        nums = []
        str1 = request.args['nums']
        for x in str1.split(','):
            nums.append(int(x))
        mode = statistics.mode(nums)
        ret = {"mode": mode, "nums":nums}
        return json.dumps(ret), 200, {"Content-Type":'application/json'}
    return "missing parameters",400
        

app.run(host='127.0.0.1', port=3001)