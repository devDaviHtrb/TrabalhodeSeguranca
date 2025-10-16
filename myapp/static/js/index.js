function queryBar() {
  const endereco = document.getElementById("enderecoInput").value.trim();
  const msgLabel = document.getElementById("msg");
  if (!endereco) {
    msgLabel.innerText = "Coloque o endereço";
    return;
  }

  const encodedEndereco = encodeURIComponent(endereco);

  fetch(`/verifyBar/${encodedEndereco}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erro: " + response.status);
      }
      return response.json();
    })
    .then((data) => {
      const resultado = document.getElementById("resultado");
      if (data.error) {
        resultado.innerHTML = `<p>Erro: ${data.error}</p>`;
      } else if (Object.keys(data).length > 0) {
        resultado.innerHTML = `
          <h3>Resultado da Consulta:</h3>
          <div>
            <p><strong>Reputação:</strong> ${data.reputacao}</p>
            <p><strong>Endereço:</strong> ${data.endereco}</p>
            <p><strong>Status:</strong> ${data.condicao}</p>
          </div>`;
        if (data.reputacao > 3) {
          resultado.innerHTML += `<p> Recomendado</p>`;
        } else {
          resultado.innerHTML = `<p>Não Recomendado</p>`;
        }
      } else {
        resultado.innerHTML = "<p>Nenhum bar encontrado.</p>";
      }
    })
    .catch((error) => {
      document.getElementById(
        "resultado"
      ).innerHTML = `<p>Erro: ${error.message}</p>`;
    });
}
