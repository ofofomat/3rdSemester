from flask import Flask
from graphql_server.flask import GraphQLView
from schema import schema

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello there"


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)


if __name__ == '__main__':
    app.run(debug=True, port='5000', host='0.0.0.0')
