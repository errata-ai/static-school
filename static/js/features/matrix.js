$(document).ready(function() {
  $('#matrix').DataTable({
    paging: false,
    ordering: false,
    info: false,
    searching: false,
    scrollX: true,
    dom: 'Bfrtip',
    buttons: [{extend: 'colvis', columns: ':not(.noVis)'}]
  });
});
