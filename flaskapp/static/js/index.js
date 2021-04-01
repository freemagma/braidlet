var table = $("#table");
var add_btn = $("#add_braid");
var submit_btn = $("#submit_query");
var query = $("#query_dropdown");
var query_btn = $("#dropdownMenuButton");
var q_group = $("#query_group");

$(function () {
  updateQuery();
  add_btn.click(() => {
    $("<input/>")
      .attr("type", "hidden")
      .attr("name", "query_type")
      .attr("value", query_type)
      .appendTo("#form");
    $("<input/>")
      .attr("type", "hidden")
      .attr("name", "new_braid_num")
      .attr("value", new_braid_num)
      .appendTo("#form");
    $("<input/>")
      .attr("type", "hidden")
      .attr("name", "add_braid")
      .attr("value", $("#new_braid").val())
      .appendTo("#form");
    return true;
  });

  submit_btn.click(() => {
    $("<input/>")
      .attr("type", "hidden")
      .attr("name", "query_type")
      .attr("value", query_type)
      .appendTo("#form");
    $("<input/>")
      .attr("type", "hidden")
      .attr("name", "query")
      .attr("value", true)
      .appendTo("#form");
    let inputs = $(".q_input");
    $(".q_input").each((ix, node) => {
      $("<input/>")
        .attr("type", "hidden")
        .attr("name", "input_" + ix)
        .attr("value", node.value)
        .appendTo("#form");
    });
    return true;
  });

  query.click((event) => {
    query_type = event.target.text;
    updateQuery();
  });
});

function updateQuery() {
  query_btn.text(query_type);

  q_group.children().each((_, child) => {
    if (child.type == "text") child.remove();
  });
  for (let i = queries[query_type]; i > 0; i--) {
    let textbox = document.createElement("input");
    textbox.type = "text";
    textbox.classList = ["form-control q_input"];
    textbox.id = "q_input";
    textbox.placeholder = "Input " + i;
    q_group.children()[0].after(textbox);
  }
}
