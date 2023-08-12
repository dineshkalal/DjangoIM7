ORM....
==========LoginSystem============
LoginForm->	Username,Password->Submit
SignupForm->FName,LName,Email,	Username,Password,ConfirmPass
Model:loginModel->FName,LName,Email,
Usename,Password
urls->login,signup,loginchk,savedata
views->login,signup,loginchk,savedata,

def signup()
	return render(signup.html)#signupform
def savedata()
	fname=request.GET['fname']
	lname=request.GET['lname']
	if(pass!=cpass)
		return Htt
	else:
		data= LoginModel(fname=fname,lname=lname)
		data.save()
		return render(login.html)
def login():
    return render(login.html)#loginform

def loginchk():
	uname=request.GET('uname')
	pass=request.GET('pass')
	
	data= LoginModel.objects.all()
	#select *from loginModel
data=LoginModel.object.filter(uname=uname)
select * from LoginModel where uname=uname;
	for d in data:
	
	if (d.uname=uname and d.pass==pass)
		return render('home.html',{'Name':d.uname})





