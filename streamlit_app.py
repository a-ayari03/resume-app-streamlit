import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Alexandre Ayari
##### *My Resume* 
''')

image = Image.open('cropped_image.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Junior Data driven student looking for experience in Data science and Data Analyst field
- Experience in Multinational electronics and semiconductors manufacturer 
- Experience as Research trainee in the field of geophysics
- Self-taught developper
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background: linear-gradient(145deg, rgba(217,31,31,1) 0%, rgba(0,88,254,1) 100%);">
  <a class="navbar-brand" href="https://www.linkedin.com/in/alexandre-a-45a297153/" target="_blank">Alexandre Ayari</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Work Experience
''')

txt('**Data analytics / Data scientist**, STMicroelectronics, Rousset - France | **Alternance**',
"Nov 22'-Current")
st.markdown('''
Integration of the Quality team, managing the digitalisation process for `10` people
- Creation of ETL & Dashboard reporting (`Spotfire`)
- Roadmap and project management
- Creation and administration of Database (`Oracle`, `SQL`)
- Automation and extraction process (Python)
- Computer Vision and NLP projects (`Tensorflow`, `OpenCv`, `Spacy`) 
''')

txt('**Data Scientist / Analyst**, Remote | [**Freelance**](https://www.malt.fr/profile/alexandreayari)',
"May 22'-Current")
st.markdown('''
Freelance mission, setting up from scratch a database with dashboard report using web framework Python 
- Setting up a database with a csv file update pipeline (Python, `MariaDB`, SQL)
- Automation and extraction process (Python)
- Dashboard reporting using `Django` framework and `Dash`
- Data cleaning and analysis 
'''
)

txt('**Research Intern**, *Saclay University*, Paris, France | **Intern**',
"Feb 21'-Aug 21'")
st.markdown('''
Master's thesis in Earth Sciences, research intern in hydrogeology field
Calibration of temperatures measured by drone on a test plot located in the natural park of La Bassée (Seine River Basin) entirely with Python :
- Classification, segmentation, interpolation of spatial data using K-means (`Open CV` , `Scikit-learn`, geostatistics, matplotlib)
- Introduction to the use of neural networks (`TensorFlow`)
'''
)

#####################
st.markdown('''
## Education
''')

txt('**Msc in Data Science and AI** , *Data ScienceTech Institute*, France',
'2021-2023')
st.markdown('''
##### Main topics to cover :
- Statistics, Machine Learning and Deep Learning algorithms (`R`, Python)
- Cloud Computing (`AWS`)
- Data Wrangling (`SQL`)
- Software Engineering (C, C++, Python)
- Big Data: `Hadoop` ecosystem and `Spark`
- Two professional certifications (`AWS` Solutions Architect Associate and SAS Enterprise Miner)
''')

txt('**Master of Earth Science** (Geophysics), *Sorbonne Sciences University*, Paris, France',
'2019-2021')

txt('**Bachelor of Earth Science** (Geophysics), *Sorbonne Sciences University*, Paris, France',
'2016-2019')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `Dash`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Computer Vision & NLP libraries', '`OpenCV`, `Spacy`')
txt3('Web development', '`Django`')
txt3('Model deployment', '`streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/alexandre-a-45a297153/')
txt2('GitHub', 'https://github.com/a-ayari03/')
txt2('Malt', 'https://www.malt.fr/profile/alexandreayari')
