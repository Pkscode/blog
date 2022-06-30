Follow these steps to run the file :
1) activate the blog-env environment by using command:
source blog-env/Scripts/activate (if you're using ubuntu else remove "source" (windows user))
3) install the requirements using the same in command line :
pip install -r requirements.txt
4) run the project using the below command :
uvicorn main:app --reload
5) see the output in local host 
