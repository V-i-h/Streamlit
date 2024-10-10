import streamlit as st
import random 
# 1- Crie um algoritmo que descubra um número secreto!

# 2- Criar o número secreto

# 3- Título na aplicação 
st.title("Jogo do número secreto")

if 'numero_secreto' not in st.session_state:
     st.session_state.numero_secreto = random.randint(1, 100)
      
    
# 4- Dar uma mensagem de boas vindas
st.write("Boas-vindas ao jogo do número secreto")
# 5- Receber o chute do usuário

st.write(f'O número secreto: {st.session_state.numero_secreto}')
chute= st.number_input("Escolha um número de 1 a 100:", min_value=1, max_value=100)
# 6- Verificar o chute com o número secreto

if st.button('Verificar'):
     if chute == st.session_state.numero_secreto: 
     # 7- Mostrar uma mensagem personalizada
         st.balloons()
         st.success(f'Isso aí! Você descobriu o número secreto: {st.session_state.numero_secreto}')
        
     else:
      st.error(f'Infelizmente você errou! Tente novamente! Número correto : {st.session_state.numero_secreto}')


