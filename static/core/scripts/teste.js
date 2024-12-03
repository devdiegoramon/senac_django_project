    // Captura do formulário e dos elementos de resumo
    const financeForm = document.getElementById('financeForm');
    const rendaMensal = document.getElementById('rendaMensal');
    const gastosFixos = document.getElementById('gastosFixos');
    const gastosVariaveis = document.getElementById('gastosVariaveis');
    const investimentos = document.getElementById('investimentos');
    const dividas = document.getElementById('dividas');
    const objetivoFinanceiro = document.getElementById('objetivoFinanceiro');
    
    financeForm.addEventListener('submit', function(e) {
        e.preventDefault();  // Impede o envio do formulário
        
        // Coletando os dados do formulário
        const income = parseFloat(document.getElementById('income').value);
        const fixedExpenses = parseFloat(document.getElementById('fixedExpenses').value);
        const variableExpenses = parseFloat(document.getElementById('variableExpenses').value);
        const investmentsValue = parseFloat(document.getElementById('investments').value);
        const debts = parseFloat(document.getElementById('debts').value);
        const financialGoal = document.getElementById('financialGoal').value;
        
        // Atualizando o resumo com os valores inseridos
        rendaMensal.textContent = income.toFixed(2);
        gastosFixos.textContent = fixedExpenses.toFixed(2);
        gastosVariaveis.textContent = variableExpenses.toFixed(2);
        investimentos.textContent = investmentsValue.toFixed(2);
        dividas.textContent = debts.toFixed(2);
        objetivoFinanceiro.textContent = financialGoal || 'Não especificado';
    });


