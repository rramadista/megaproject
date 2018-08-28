// Data Tables
$(document).ready(function () {
    $('#mytable').DataTable({
        dom: 'Bfrtip',
        buttons: {
            dom: {
                button: {
                    tag: 'button',
                    className: 'waves-effect waves-light btn btn-small'
                }
            },
            buttons: [{
                    text: '<i class="far fa-copy"></i>',
                    extend: 'copy',
                },
                {
                    text: '<i class="far fa-file-excel"></i>',
                    extend: 'excel',
                },
                {
                    text: '<i class="far fa-file-pdf"></i>',
                    extend: 'pdf',
                },
                {
                    text: '<i class="fas fa-print"></i>',
                    extend: 'print',
                },
                {
                    text: '<i class="fas fa-columns"></i>',
                    extend: 'colvis',
                }
            ]
        },
        colReorder: true,
        keys: {
            columns: ':not(:last-child)'
        }
    });
});

// Materialize JS
// Sidenav
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});

// Parallax
const parallax = document.querySelectorAll('.parallax');
M.Parallax.init(parallax, {});

// Dropdown
const dropdown = document.querySelector('.dropdown-trigger');
M.Dropdown.init(dropdown, {});

// Collapsible
const collapsible = document.querySelector('.collapsible');
M.Collapsible.init(collapsible, {
    accordion: false
});

// Tooltips
const tooltips = document.querySelector('.tooltipped');
M.Tooltip.init(tooltips, {});

// Carousel
const carousel = document.querySelectorAll('.carousel');
M.Carousel.init(carousel, {});

// Modals
const modals = document.querySelectorAll('.modal');
M.Modal.init(modals, {});

// Date Picker
const datepicker = document.querySelectorAll('.datepicker');
M.Datepicker.init(datepicker, {});

// Form Select
const select = document.querySelectorAll('select');
M.FormSelect.init(select, {});

// Dropify JS
$('.dropify').dropify();

$(document).ready(function () {
    M.updateTextFields();
});