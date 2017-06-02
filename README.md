REGTAG

The purpose of this project is to identify how similar different regulatory papers are across different country's regulatory environments
as well as their likeness towards major regulatory doctrines like MiFID.

In this example, i have used "Regulatory technical and implementing standards – MiFID II" to train a Doc2Vec model using the Gensim package.
I have then tried to find cosine similarites between smaller regulatory documents (consultation papers) to see how similar 2 documents are. 
Given the model has been trained on a larger, more technical paper, the similarities should provide some insight into regualtions that are similar
to each other.
     
p.s 
My sincere apologies that a small part of this is hardcoded and you will run into some issues. After download the repository, you will need to open
main.py and edit 2 objects:

1) LINE 14: "os.chdir("C:\\Users\\VickSella\\Desktop\\regtag\\REGTAG-final")" - please change the root dir "C:\\Users\\VickSella\\Desktop\\" to where the 
   download is.

2) LINE 18: "mydir="C:\\Users\\VickSella\\Desktop\\regtag\\REGTAG-final"" - same as point 1.       
