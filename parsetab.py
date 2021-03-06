
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightDIVIDEASSIGN DIVIDE EQUALS EXEC ID INPUT LPAREN MODULE NAME NEWLINE NODE OUTPUT PACK RPARENmodule : MODULE name LPAREN input_list output_list node_list assign_list RPARENmodule : errorinput : INPUT topicinput_list : input_list input\n                  | inputoutput : OUTPUT topicoutput_list : output_list output\n                   | outputnode : NODE LPAREN node_info RPARENnode_info : NAME name input_list output_list pack execnode_list : node_list node\n                 | nodeexec : EXEC namepack : PACK nameassign : ASSIGN topic EQUALS topicassign_list : assign_list assign\n                   | assigntopic : topic DIVIDE name\n             | DIVIDE namename : IDempty : '
    
_lr_action_items = {'DIVIDE':([4,8,13,14,20,22,26,28,33,36,38,],[-20,15,15,21,21,-19,15,-18,21,15,21,]),'PACK':([4,10,16,20,22,28,39,],[-20,-8,-7,-6,-19,-18,40,]),'error':([0,],[2,]),'NAME':([23,],[29,]),'INPUT':([4,6,7,9,12,14,22,28,34,37,],[-20,8,8,-5,-4,-3,-19,-18,8,8,]),'NODE':([4,10,11,16,18,19,20,22,27,28,35,],[-20,-8,17,-7,17,-12,-6,-19,-11,-18,-9,]),'EQUALS':([4,22,28,33,],[-20,-19,-18,36,]),'ASSIGN':([4,18,19,22,24,25,27,28,31,35,38,],[-20,26,-12,-19,26,-17,-11,-18,-16,-9,-15,]),'MODULE':([0,],[3,]),'RPAREN':([4,22,24,25,28,30,31,38,44,45,],[-20,-19,32,-17,-18,35,-16,-15,-10,-13,]),'OUTPUT':([4,7,9,10,11,12,14,16,20,22,28,37,39,],[-20,13,-5,-8,13,-4,-3,-7,-6,-19,-18,13,13,]),'LPAREN':([4,5,17,],[-20,6,23,]),'ID':([3,15,21,29,40,43,],[4,4,4,4,4,4,]),'$end':([1,2,32,],[0,-2,-1,]),'EXEC':([4,41,42,],[-20,43,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input_list':([6,34,],[7,37,]),'assign_list':([18,],[24,]),'output':([7,11,37,39,],[10,16,10,16,]),'output_list':([7,37,],[11,39,]),'node_list':([11,],[18,]),'node_info':([23,],[30,]),'input':([6,7,34,37,],[9,12,9,12,]),'topic':([8,13,26,36,],[14,20,33,38,]),'module':([0,],[1,]),'assign':([18,24,],[25,31,]),'node':([11,18,],[19,27,]),'pack':([39,],[41,]),'name':([3,15,21,29,40,43,],[5,22,28,34,42,45,]),'exec':([41,],[44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> MODULE name LPAREN input_list output_list node_list assign_list RPAREN','module',8,'p_module','parse.py',17),
  ('module -> error','module',1,'p_program_error','parse.py',27),
  ('input -> INPUT topic','input',2,'p_input','parse.py',32),
  ('input_list -> input_list input','input_list',2,'p_input_list','parse.py',36),
  ('input_list -> input','input_list',1,'p_input_list','parse.py',37),
  ('output -> OUTPUT topic','output',2,'p_output','parse.py',45),
  ('output_list -> output_list output','output_list',2,'p_output_list','parse.py',49),
  ('output_list -> output','output_list',1,'p_output_list','parse.py',50),
  ('node -> NODE LPAREN node_info RPAREN','node',4,'p_node','parse.py',58),
  ('node_info -> NAME name input_list output_list pack exec','node_info',6,'p_node_info','parse.py',62),
  ('node_list -> node_list node','node_list',2,'p_node_list','parse.py',71),
  ('node_list -> node','node_list',1,'p_node_list','parse.py',72),
  ('exec -> EXEC name','exec',2,'p_exec','parse.py',80),
  ('pack -> PACK name','pack',2,'p_pack','parse.py',84),
  ('assign -> ASSIGN topic EQUALS topic','assign',4,'p_assign','parse.py',88),
  ('assign_list -> assign_list assign','assign_list',2,'p_assign_list','parse.py',94),
  ('assign_list -> assign','assign_list',1,'p_assign_list','parse.py',95),
  ('topic -> topic DIVIDE name','topic',3,'p_topic','parse.py',103),
  ('topic -> DIVIDE name','topic',2,'p_topic','parse.py',104),
  ('name -> ID','name',1,'p_name','parse.py',111),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',115),
]
