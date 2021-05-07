from flask import Flask,render_template,request,jsonify,redirect
app=Flask(__name__)
import webbrowser
@app.route("/<user>",methods=["GET","POST"])
def root(user):
    if request.method=="GET":
        return render_template("home.html",username=user)
    elif request.method=="POST":
        val=request.form.get("fname")
    if val is not None:
        return jsonify({"yey rha":val})
    return redirect("/")
   

if __name__=="__main__":
    # webbrowser.open("https://localhost:6060")

    app.run(use_reloader=True,debug=True)
