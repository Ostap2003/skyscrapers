# Skyskraper game

**skyskraper.py** recieves board and checks its complience with the [rules](https://cms.ucu.edu.ua/mod/vpl/view.php?id=163068&userid=6019) of the game.

You can find some tests in **data** folder.

<br></br>

#### Short explanation of the rules:

Skyscrapers is a logic game of the placement of houses. In this game you need to place houses of different heights on the game board, so that the number of visible houses from a certain position (the number with the arrow is a hint) was equal to the number in the hint. The arrow indicates the direction in which you want to look.

**3-D version of the game board for better uderstanding:**

<div align="left">
  <img src="https://lh4.googleusercontent.com/XE1q8uFnyJTosIxT_f8ewQvv0m80xR62MLxwF6z-WgBbVwWAzlaXAg3YET6xupGIdmMkDzI1sHngyELHsw2IK7sFdWVGEsWwOGaUMK4006G_pFWFl5cBZXkJLqe3YY6SEHaZysNL"><br>
</div>


So, the game board is a square N x N, with hints on the sides. The object of the game is to place a skyscraper 1 to N high in each cell so that:

- No two skyscrapers in a row were the same height.
- No two skyscrapers in the column were the same height.
- The number of visible skyscrapers from a certain direction (hint with an arrow) was equal to the number in the hint. Note that the taller skyscrapers obscure the visibility of the lower skyscrapers behind the taller skyscrapers.

#### Example of the game board:

<div align=left>
    <img src='https://lh5.googleusercontent.com/Zg_CsfS_CF_8iU9gzEPdrPRMTLOQKSNTMdX1fUwr5RUqeHc8vNplbhCKQw0cfwKlfo5plEBkH8LmUzi90NqIur_uI3tYyCZeKpKBSNdwMxTrH_nO3BadBRwCPgs9vI1JsiS_x8tf'>
<div>
