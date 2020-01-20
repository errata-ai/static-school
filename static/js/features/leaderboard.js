var mdList = new List('ssg-list', {
    valueNames: ['time'],
    listClass: 'list-md'
});

var adocList = new List('ssg-list', {
    valueNames: ['time'],
    listClass: 'list-adoc'
});

var rstList = new List('ssg-list', {
    valueNames: ['time'],
    listClass: 'list-rst'
});

mdList.sort('time', {
    order: 'asc'
});

$(".filter-select").change(function () {
    var format = $(this).val();
    if (format === "md") {
        $("#md").removeClass("d-none");
        $("#adoc,#rst").addClass("d-none");
        mdList.sort('time', {
            order: 'asc'
        });
    } else if (format === "adoc") {
        $("#adoc").removeClass("d-none");
        $("#md,#rst").addClass("d-none");
        adocList.sort('time', {
            order: 'asc'
        });
    } else {
        $("#rst").removeClass("d-none");
        $("#md,#adoc").addClass("d-none");
        rstList.sort('time', {
            order: 'asc'
        });
    }
});
