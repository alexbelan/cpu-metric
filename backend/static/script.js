let btnSortPerformance = document.querySelector('.btn-sort-performance');
let btnSortPerformanceArrow = document.querySelector('.btn-sort-performance span');
let typeSortPerformance = true;

btnSortPerformance.addEventListener("click", () => {
    if (typeSortPerformance === true) {
        let sortedRows = Array.from(table.rows).slice(1)
            .sort((rowA, rowB) => +rowA.cells[1].innerHTML > +rowB.cells[1].innerHTML ? 1 : -1);
        table.tBodies[0].append(...sortedRows);
        typeSortPerformance = false
        btnSortPerformanceArrow.innerHTML = "&or;"
    } else if (typeSortPerformance === false) {
        let sortedRows = Array.from(table.rows).slice(1)
            .sort((rowA, rowB) => +rowA.cells[1].innerHTML < +rowB.cells[1].innerHTML ? 1 : -1);
        table.tBodies[0].append(...sortedRows);
        btnSortPerformanceArrow.innerHTML = "&and;"
        typeSortPerformance = true
    }
})


