
function searchTable() {
  let input = document.getElementById("searchInput");
  let filter = input.value.toLowerCase();
  let table = document.getElementById("fileTable");
  let rows = table.getElementsByTagName("tr");

  for (let i = 1; i < rows.length; i++) {
    let cells = rows[i].getElementsByTagName("td");
    let idCell = cells[0].textContent.toLowerCase();
    let filePathCell = cells[1].textContent.toLowerCase();

    if (idCell.includes(filter) || filePathCell.includes(filter)) {
      rows[i].style.display = "";
    } else {
      rows[i].style.display = "none";
    }
  }
}

function showDetails(id, data) {
  // Ocultar tabela principal
  document.getElementById("fileTable").style.display = "none";

  // Preencher a tabela de detalhes com dados fictícios
  let detailsBody = document.getElementById("detailsTableBody");
  detailsBody.innerHTML = "";

  data.forEach((content, i) => {
    detailsBody.innerHTML += `
      <tr>
        <td title=${content.hash}><strong>${content.hash.slice(0, 8) + "..."}</strong></td>
        <td>${content.original}</td>
        <td>${content.encrypted}</td>
        <td>${content.type}</td>
        <td>${content.line}</td>
      </tr>
    `;
  });

  // Exibir a tabela de detalhes e o botão de voltar
  document.getElementById("detailsTable").style.display = "table";
  document.getElementById("backButton").style.display = "inline-block";
}

function goBack() {
  // Ocultar a tabela de detalhes e o botão de voltar
  document.getElementById("detailsTable").style.display = "none";
  document.getElementById("backButton").style.display = "none";

  // Mostrar a tabela principal
  document.getElementById("fileTable").style.display = "table";
}
