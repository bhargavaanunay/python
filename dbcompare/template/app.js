var app = angular.module('app', ['ui.grid', 'ui.grid.cellNav', 'ui.grid.edit', 'ui.grid.resizeColumns', 'ui.grid.pinning']);
app.controller('MainCtrl',  ['$scope', '$http', '$timeout', '$interval', function ($scope, $http, $timeout, $interval) {

  $scope.tabs = {selectedTab:-1};
  $scope.gridOptions = {};
  $scope.gridOptions.data = 'myData';
  

  $scope.gridOptions.columnDefs = %%headers%%;

  // [
    
  //   { name:'name', width:100 },
  //   { name:'age', width:100},
  //   { name:'key', width:100
  // ];

  $scope.gridOptions.enableCellEditOnFocus = true;

  $scope.myData = %%data%%;
  
}]);
