$(document).ready(function () {
    getData(parseData);
});

year = parseInt($('#year').text());
query = $('#query-string').text();
console.log(query);
function getData(callback) {
    $.ajax({
        url: "http://www.bea.gov/api/data/",
        type: "get",
        dataType: "json",
        data: {
            USERID: "774A4531-7DF8-4490-87F9-B8B7A2EDA998",
            method: "GetData",
            datasetname: "RegionalData",
            KeyCode: query,
            GeoFIPS: "STATE",
            Year: year,
            ResultFormat: "json"
        },
        success: function (data) {
            makeHeader(data);
            makeFooter(data);
            callback(data.BEAAPI.Results.Data)
        },
        error: function (err) {
            console.log(err);
            $('#chart').html('<h3>No data matches that query</h3>');
            inputHandler();
        }
    });
}

function makeHeader(data) {
    $('#public-table').text(data.BEAAPI.Results.PublicTable + " for " + year);
    $('#statistic').text(data.BEAAPI.Results.Statistic);
}

function makeFooter(data) {
    notes = data.BEAAPI.Results.Notes;
    for (var i = 0; i < notes.length; i++) {
        $('footer').append("<p><span><small>" + notes[i].NoteRef + notes[i].NoteText);
    }
}

function parseData(data) {

    var parsedData = [];

    for (var i = 0; i < data.length; i++) {
        var label = data[i].GeoName,
            value = data[i].DataValue;
        var obj = {"label": label, "value": value};
        parsedData.push(obj);
    }

    var dataSets = orderData(parsedData);
    inputHandler(dataSets);

}
Array.prototype.remove = function (from, to) {
    var rest = this.slice((to || from) + 1 || this.length);
    this.length = from < 0 ? this.length + from : from;
    return this.push.apply(this, rest);
};


function orderData(data) {
    data.remove(0)
    var dataSets = {
        byAlpha: _.sortBy(data, function (d) {
            return d.label
        }),
        byIncome: _.sortBy(data, function (d) {
            return parseInt(d.value);
        }),
        standard: data
    };
    return dataSets;
}

function inputHandler(dataSets) {
    jwerty.key('1', function () {
        $('#display').text("State-Region");
        drawData(dataSets.standard.reverse());
    });
    jwerty.key('2', function () {
        $('#display').text("Numerical");
        drawData(dataSets.byIncome.reverse());
    });
    jwerty.key('3', function () {
        $('#display').text("Alphabetical");
        drawData(dataSets.byAlpha.reverse());
    });
    jwerty.key('shift+↓', function () {
        year--;
        changeUrl();
    });
    jwerty.key('shift+↑', function () {
        year++;
        changeUrl();
    });
    jwerty.key('shift+↖', function () {
        year += 10;
        changeUrl()
    });
    jwerty.key('shift+↘', function () {
        year -= 10;
        changeUrl()
    });
}

function changeUrl() {
    var url = location.origin + "/income/" + year + "/" + query;
    location.assign(url);
}

function drawData(data) {
    $('#chart').css('height', window.innerHeight / 2);
    nv.addGraph(function () {
        var chart = nv.models.discreteBarChart()
            .x(function (d) {
                return d.label;
            })
            .y(function (d) {
                return parseInt(d.value);
            })
            .staggerLabels(true)
            .tooltips(true)
            .showValues(false);

        d3.select('#chart svg')
            .datum([
                {
                    key: "Cumulative Data",
                    values: data
                }
            ])
            .transition().duration(5000)
            .call(chart);

        nv.utils.windowResize(chart.update);
        nv.utils.keyup(chart.update);

        return chart
    });
}

