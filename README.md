create env

'''bash
conda create -n winq python=3.7 -y
'''

activate env

'''bash
conda activate winq
'''

create requirements.txt file

pip install the requirements

'''bash 
pip install -r requirements.txt
'''

download the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

git init

initialize dvc
'''bash
dvc init
'''

to track our data we use
'''bash
dvc add data_given/winequality.csv
'''from the above command following will be requested to add
  git add 'data_given\winequality.csv.dvc' 'data_given\.gitignore'

  
To add whatever is present in my current working directory addl to the staging area of git
git add .