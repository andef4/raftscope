/* jshint globalstrict: true */
/* jshint browser: true */
/* jshint devel: true */
/* jshint jquery: true */
/* global util */
'use strict';

var makeState = function(initial) {
  var checkpoints = [];
  var maxTime = 0;
  var prev = function(time) {
      return util.greatestLower(checkpoints,
                                function(m) { return m.time > time; });
  };
  var self = {
    current: initial,
    _checkpoints: checkpoints,
    getMaxTime: function() {
      return maxTime;
    },
    init: function() {
      checkpoints.push(util.clone(self.current));
    },
    fork: function() {
      var i = prev(self.current.time);
      while (checkpoints.length - 1 > i)
        checkpoints.pop();
      maxTime = self.current.time;
    },
    rewind: function(time) {
      self.current = util.clone(checkpoints[prev(time)]);
      self.current.time = time;
    },
    base: function() {
      return checkpoints[prev(self.current.time)];
    },
    advance: function(time) {
      maxTime = time;
      self.current.time = time;
      if (self.updater(self))
        checkpoints.push(util.clone(self.current));
    },
    save: function() {
      checkpoints.push(util.clone(self.current));
    },
    seek: function(time) {
      if (time <= maxTime) {
        self.rewind(time);
      } else if (time > maxTime) {
        self.advance(time);
      }
    },
    updater: function() { return false; },
  };
  self.current.time = 0;
  return self;
};