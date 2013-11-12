(function (window) {
    var Sorter = {
        byAlpha: function (data, key) {
            list = data.slice(0);
            list.sort(function (a, b) {
                var x = a[key].substr(0, 1).toLowerCase();
                var y = b[key].substr(0, 1).toLowerCase();
                return x < y ? -1 : x > y ? 1 : 0;
            });
            return list;
        },
        byNumber: function (data, key) {
            list = data.slice(0);
            list.sort(function (a, b) {
                return a[key] - b[key];
            });
            return list
        }
    };
    window.Sorter = Sorter

})(window);