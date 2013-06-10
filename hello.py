from flask import Flask, render_template, request, redirect
testapp = Flask(__name__)

testapp.vars={}

testapp.questions={}
testapp.questions['question']=('moo','poo','goo')
testapp.questions['Which fruit do you like best?']=('banana','mango','pineapple')
testapp.questions['Do you like cupcakes?']=('yes','no','maybe')
testapp.nquestions=len(testapp.questions)

@testapp.route('/index', methods=['GET', 'POST'])
def index():
	nquestions=testapp.nquestions
	if request.method == 'GET':
		return render_template('userinfo.html', num=nquestions)
	else:
		#request is likely to be a post
		testapp.vars['name1'] = request.form['name']
		testapp.vars['age'] = request.form['age']
		testapp.vars['gender'] = request.form['gender']

		#write file containing user information
		f = open('%s_%s.txt'%(testapp.vars['name1'], testapp.vars['age']),'w')
		f.write('Name: %s\n'%(testapp.vars['name1']))
		f.write('Age: %s\n\n'%(testapp.vars['age']))
		f.write('Gender: %s\n'%(testapp.vars['gender']))
		f.close()
		
		return redirect('/main')

@testapp.route('/scaffold')


@testapp.route('/main')
def main():
	if len(testapp.questions) == 0: 
		return render_template('thanks.html')
	return redirect('/next')

@testapp.route('/next', methods=['GET'])
def nextGet():
	#helper variables
	n = testapp.nquestions-len(testapp.questions)+1
	q = testapp.questions.keys()[0]
	a1, a2, a3 = testapp.questions.values()[0] #returns answers to q 
		
	testapp.currentq = q

	return render_template('layout.html',num=n,question=q,ans1=a1,ans2=a2,ans3=a3)
	return redirect('/thanks')
		
@testapp.route('/next',methods=['POST'])
def nextPost():
	#append chosen answers
	f = open('%s_%s.txt'%(testapp.vars['name1'],testapp.vars['age']),'a')
	f.write('Question: %s\n'%(testapp.currentq))
	f.write('Answer: %s\n'%(request.form['answer'])) #this was the 'name' on layout.html
	f.close()

	#delete question from dictionary (not sure about this)
	del testapp.questions[testapp.currentq]

	return redirect('/main')

@testapp.route('/thanks',methods=['POST'])
def thanks():
	return render_template('thanks.html')

if __name__ == "__main__":
	testapp.run(debug=True)