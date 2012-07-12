function purchase( tradeGood ) {
  $.ajax({
    type: 'POST',
    url: 'tradingNegotiateTradeGood',
    data: { item: tradeGood },
    success: function( data, textStatus, jqXHR ) {
      var button = $( '#' + tradeGood );
      var textBox = $( '<input>' ).attr( 'type', 'text' );
      textBox.attr( 'value', '0' );
      textBox.attr( 'name', tradeGood );
      button.replaceWith( textBox );
      $( '#' + tradeGood + 'Cell' ).text( data.cost );
    },
    dataType: 'json',
  })
}
