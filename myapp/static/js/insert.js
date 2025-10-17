function insertBar() {
  const reputacao = document.getElementById("reputacaoInput").value;
  const endereco = document.getElementById("enderecoInput").value;
  const condicao = document.getElementById("condicaoInput").value;
  const nome = document.getElementById("NomeInput").value;

  if (!reputacao || !endereco || !condicao) {
    document.getElementById("msg").innerText = "preencha todos os campos";
    return;
  }

  fetch("/inputBar", {
    method: "POST",

    body: new URLSearchParams({
      nome: nome,
      reputacao: reputacao,
      endereco: endereco,
      condicao: condicao,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erro ao inserir dados: " + response.status);
      }
      return response.json();
    })
    .then((data) => {
      document.getElementById("reputacaoInput").value = "";
      document.getElementById("enderecoInput").value = "";
      document.getElementById("condicaoInput").value = "";
      document.getElementById("NomeInput").value = "";

      document.getElementById("msg").innerText = data;
    })
    .catch((error) => {
      console.log(error);
    });
}
