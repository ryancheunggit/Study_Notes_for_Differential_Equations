function H = dfstart

% DFSTART is a function m-file that is read when DFIELD5 
%         is started and which inputs certain data that 
%         are used to change defaults.  Only four items 
%         may be changed.  To do so it is necessary to enter 
%         one or more of the following lines.  The entries 
%         here are the defaults.

H = [];   % DO NOT REMOVE THIS LINE!
          % If there is a dfstart.m file, it must contain this line.


H.style = 'display';	% Must be 'white', 'black', or 'display'. 
                        % 'white' is the default.
                     

H.size = 18;	     % Any number is allowed.  This is the 
                     % main font size used in DFIELD5.  It 
                     % determines the size of all windows,
                     % and everything else.
		     % The default is 10
                     
% H.npts = 20;       % The number of field points per line.  
                     % The default = 20.

% H.solver = 'Euler';  % The choices are 'Euler', 'Runge-Kutta 2', 
                       % 'Runge-Kutta 2', and 'Dormand-Prince'.
		       % The default is 'Dormand-Prince'.
