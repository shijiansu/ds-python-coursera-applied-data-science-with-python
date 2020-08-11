/**
 * Note: This plugin was written by cbrooks@umich.edu to support a course-specific feature. 
 */
define(['base/js/events', 'jquery'], function (events, $) {
    console.log("Michigan custom assignment extension started.");
    var assignment_server = "https://o9s6k5zl24.execute-api.us-east-1.amazonaws.com/prod/c2a2";

    function load_assignment_data() {
        $.ajax({
            url: assignment_server,
            type: 'GET',
            data: 'notebookid=' + encodeURI(document.location), // "http://localhost:8888/notebooks/assignment2.ipynb"
            dataType: 'jsonp',
            success: function (data) {
                //Only do something with the file returned if there is no data already in the notebook
                if (Jupyter.notebook.get_cells().length <= 1) {
                    Jupyter.notebook.insert_cell_above('code', 0).set_text(data['assignment_code_template']);
                    Jupyter.notebook.insert_cell_above('markdown', 0).set_text(data['assignment_description_template']);
                    Jupyter.notebook.execute_all_cells();
                }
            },
            error: function (e) {
                console.log(e.toString());
            }
        });
    }

    function load_ipython_extension() {
        if (location.pathname.split("/")[location.pathname.split("/").length - 1] == "Assignment2.ipynb"){
            window.setTimeout(load_assignment_data, 2000);
        }
        if (location.pathname.split("/")[location.pathname.split("/").length - 1] == "Assignment4.ipynb"){
            window.setTimeout(load_assignment_data, 2000);
        }
        if (location.pathname.split("/")[location.pathname.split("/").length - 1] == "Assignment0.ipynb"){
            window.setTimeout(load_assignment_data, 2000);
        }
    }

    return {
        load_ipython_extension : load_ipython_extension,
    };
});