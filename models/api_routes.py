from flask import request
from flask.json import jsonify
from flask_cors import CORS
from flask import Blueprint
from models.questiongenerator import QuestionGenerator

api = Blueprint(
    'api', 'api', url_prefix='/')
CORS(api)

'''
{
    "chapter": string,
}


'''


@api.route("/qna")
def qna():
    #df = pd.read_csv('final_data.csv')
    #chapter = df.iloc[3]['0']
    request_data = request.get_json()
    chapter = request_data["chapter"]
    #file = open("book.txt", 'w')
    # file.write(str(chapter))
    qg = QuestionGenerator()
    qa_list = qg.generate(chapter)
    print(qa_list)
    return jsonify(qa_list)


'''qa_list = subprocess.check_output(
        ["python", "qna_model/run_qg.py", "--text_dir", "book.txt"])
    qa_list = qa_list.decode('utf8').replace("'", '"')
    qa_list = json.loads(qa_list)'''

''
