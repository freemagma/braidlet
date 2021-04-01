from flask import Flask, render_template, redirect, session, request
from .queries import QUERIES, QUERY_FUNCS, DEFAULT_INIT_QUERY
from .parse_braid import parse_braid


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    @app.route("/", methods=["GET", "POST"])
    def index():
        init_query = DEFAULT_INIT_QUERY
        if "braids" not in session:
            braids = [
                {"id": str(0), "input_form": str([0, 1, 2, 3])},
                {"id": str(1), "input_form": str([0] * 50)},
            ]
        else:
            braids = session["braids"]

        result = None
        if request.method == "POST":
            print(dict(request.form))
            if "query_type" in request.form:
                # preserve current query selection
                init_query = request.form["query_type"]
            if "add_braid" in request.form:
                # user requests to add a braid to form
                new_braid_num = request.form["new_braid_num"]
                if int(new_braid_num) == len(braids):
                    braid = parse_braid(request.form["add_braid"], braids)
                    braid_dct = {
                        "id": new_braid_num,
                        "input_form": str(
                            parse_braid(request.form["add_braid"], braids)
                        ),
                    }
                    if braid is not None:
                        braids.append(braid_dct)
            elif "query" in request.form:
                # user makes a query
                inputs = [
                    parse_braid(request.form[f"input_{i}"], braids)
                    for i in range(QUERIES[init_query])
                ]
                result = QUERY_FUNCS[init_query](*inputs)

        session["braids"] = braids
        return render_template(
            "index.html",
            braids=braids,
            queries=QUERIES,
            init_query=init_query,
            result=result,
        )

    return app