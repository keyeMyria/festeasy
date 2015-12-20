shared.directive('rands', () ->
	return {
		restrict: 'E'
		scope: {
			amountRands: '='
		}
		template: 'R{{amountRands | number: 2}}'
	}
)
