from App import app
@app.route('/')
@app.route('/index')
def index():
    return '<HTML><HEAD><TITLE>PAGE</TITLE></HEAD><BODY BACKGROUND="C:\Users\harsimar\Pictures\1280px-View_of_Lord_Nataraja_at_Temple_museum.JPG"><H1 ALIGN="CENTER">Hello World</H1><FONT FACE="TIMES NEW ROMAN" COLOR="YELLOW" SIZE="5"><P ALIGN="CENTER">This is the first line</P></FONT></BODY></HTML>'

