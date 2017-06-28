# artificial-intelligence-untref

Falta:
- Terminar lo del doble valor del AS

- Integrar el split a la matriz de q-value, y hacerlo para que diferencie sobre que par de valores se hace el split.

- Double bet: 
  1)Cuando juegue en serio (no entrenamiento) tome en cuenta al q-value correspondiente de double bet para tomar la decisión. DONE.
	PROBLEMA: cuando entrena, sospecho que no esta actualizando correctamente los valores del double bet. Puede ser?

  2)Restringir el double bet únicamente a la mano inicial. DONE
  3)Usar el bet para calcular el reward. Lo único que falta es llamar al atributo current_player_bet de blackjack_game
