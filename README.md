# artificial-intelligence-untref

Falta:
- Terminar lo del doble valor del As. DONE

- Integrar el split a la matriz de q-value, y hacerlo para que diferencie sobre que par de valores se hace el split. DONE

- Double bet: 
  1)Cuando juegue en serio (no entrenamiento) tome en cuenta al q-value correspondiente de double bet para tomar la decisión. DONE
	PROBLEMA: cuando entrena, sospecho que no esta actualizando correctamente los valores del double bet. Puede ser?

  2)Restringir el double bet únicamente a la mano inicial. DONE
  3)Usar el bet para calcular el reward. Lo único que falta es llamar al atributo current_player_bet de blackjack_game
 4) (OPCIONAL) Refactoring, mucho refactoring. Separar responsabilidades, quitar returns que no devuelven nada, armar un diseño mas legible.