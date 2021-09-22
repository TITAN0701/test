clear all;
close all;
clc;
% train1=[0 0;2 4;3 3;3 4;4 2;4 4;4 3;5 3;6 2;7 1;2 9;3 8;4 6;4 7;5 6;5 8;6 6;7 4;8 4;10 10];                                              %???据?
% group1=[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]'; 
%                                                                           
% test=[3 2;4 8;6 5;7 6;2 5;5 2];                                                    %???据

t0 = clock;                                         % 記錄現在的時間

xlsFile = 'mfcc.xlsx';
B = xlsread(xlsFile, '工作表2', 'B1:B72');		% 讀出 'Sheet2' 的全部資料

C = xlsread(xlsFile, '工作表2', 'C1:KQ72');
D = xlsread(xlsFile, '工作表5', 'B1:KP4');
predict = zeros(4);
% %SVM
% %svmModel1=svmtrain(C,B,'kernel_function','linear','shoplot',true);
% svmModel=svmtrain(B,C);
% for i = 1:4
%     % 作???，svmpredict第一????便??就可以
%     predict(i) = svmpredict(0,D(i,:),svmMode);
% end

% Logistic regression
% E=mnrfit(C,B);
% Scores = mnrval(E, D)



% Neural Network(類神經網絡)
C1=C.';
s = length(B) ;
B3 = zeros( s , 14  ) ;
for i = 1 : s 
   B3( i , B( i )  ) = 1 ;
end

B1=B3.';


% To Use GPU Calculation %
G_devi_count = gpuDeviceCount   % 有幾張 GPU卡
g = gpuDevice                     % GPU卡相關訊息
D1=D.';

% [C1,B1] = vinyl_dataset;
% Xgpu = gpuArray(single(C1));
% Tgpu = gpuArray(single(B1));

% Xgpu = gpuArray(C1);
% Tgpu = gpuArray(B1);

tic
% Deep Learning 4 Hidden layers %
net = feedforwardnet([15 60 120 60 15]);

% MLP 1 Hidden layers %
% net = feedforwardnet(200,'trainscg');

net.trainparam.show =10 ;
net.trainparam.epochs = 1000;
net.trainparam.goal = 0.001 ;
net.trainParam.lr = 0.001 ;
net.trainParam.max_fail = 100;   % Validation checks
% nnModel=train(net,Xgpu,Tgpu,'UseParallel','yes','UseGPU','only')  %B1= Target
nnModel=train(net,C1,B1,'UseParallel','yes','UseGPU','only')
y2 = nnModel(D1);
y2 = gather(y2); 
G_NN_y2=y2'
fprintf('GPU time = %g sec\n', toc);


% %% CPU %%
% D1=D.';
% net = feedforwardnet(25);                % feedforwardnet,cascadeforwardnet,timedelaynet
% net.trainparam.show = 50 ;
% net.trainparam.epochs = 50 ;
% net.trainparam.goal = 0.01 ;
% net.trainParam.lr = 0.01 ;
% nnModel=train(net,C1,B1);
% y2=nnModel(D1);
% C_NN_y2=y2'  % 預測結果準確率


TotalTime = etime(clock, t0)               % 計算所耗費的總時間