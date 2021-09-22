clear all;
close all;
clc;

t0 = clock;                                         % 記錄現在的時間


xlsFile = 'F15_MFCC_Simon.xlsx';
B = xlsread(xlsFile, 'F15_all', 'B1:B75');		    % 讀出 'F15_all' Label資料
C = xlsread(xlsFile, 'F15_all', 'C1:OL75');         % 讀出 'F15_all' 的全部資料
D = xlsread(xlsFile, 'F15_all_test', 'B1:OK15');    % 測試 'F15_all_test' 驗證聲紋比對是否正確

predict = zeros(15);                                % 預測目標個數        15種青蛙聲音辨識種類


% % SVM %
% svmModel=svmtrain (B, C);
% for i = 1:15
%      predict(i) = svmpredict(0,D(i,:),svmModel);
% end

% % SVM %
% % svmModel1=svmtrain(C,B,'kernel_function','linear','shoplot',true);
% svmModel=svmtrain(B,C);
% for i = 1:15
%     
%     predict(i) = svmpredict(0,D(i,:),svmModel);
% end


% Logistic regression(邏輯回歸)
% fprintf('CPU time = %g sec\n', toc);
% gC=gpuArray(single(C));		% Put C to GPU's memory
% gB=gpuArray(single(B));		% Put C to GPU's memory
% gD=gpuArray(single(D));
% [o1, o2] = arrayfun(@xycrull, gt) 
% gE = arrayfun(@mnrfit(gC,gB));

% % CPU Logistic regression(邏輯回歸)
% E=mnrfit(C,B);
% LR_Scores = mnrval(E, D)  % 預測結果準確率
% % gLR_S = gather(gScores);		% Put gScores to MATLAB's workspace

% %  GPU  Logistic regression(邏輯回歸)
% Xgpu = gpuArray(C);
% Tgpu = gpuArray(B);
% Kgpu = gpuArray(D);
% E=mnrfit(Xgpu,Tgpu);
% LR_Scores = mnrval(E,Kgpu)  % 預測結果準確率


% Neural Network(類神經網絡)
C1=C.';
s = length(B) ;
B3 = zeros( s , 14  ) ;
for i = 1 : s 
   B3( i , B( i )  ) = 1 ;
end

B1=B3.';


%%  To Use GPU Calculation   %%
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
net = feedforwardnet([30 60 240 60 15],'trainscg');     % R=0.99164   % trainscg, traingda[30 60 240 60 15]比trainscg效果好喔
% net = feedforwardnet([15 120 240 120 15]);            % traingda:學習率是自動可變的
% net = feedforwardnet([15 120 240 500 240 120 15]);


% MLP 1 Hidden layers %
% net = feedforwardnet(100,'trainscg');           %trainscg, traingda, traingdm

net.trainparam.show =50 ;
net.trainparam.epochs = 50000;         % Epochs:疊帶次數
net.trainparam.goal = 0.001 ;
net.trainParam.lr = 0.001 ;            % 學習率:愈小收斂速度慢，但效果穩定；同理則反之
net.trainParam.max_fail = 100;         % Validation checks: 驗證次數，次數多，Epochs會跑愈多次
% nnModel=train(net,Xgpu,Tgpu,'UseParallel','yes','UseGPU','only')  %B1= Target
nnModel=train(net,C1,B1,'UseParallel','yes','UseGPU','only')
y2 = nnModel(D1);
y2 = gather(y2);                       % 將 y2在GPU算完的值 傳回 MATLAB's(CPU平台) workspace
G_NN_y2=y2'
fprintf('GPU time = %g sec\n', toc);


% %%  使用電腦本身的 CPU 做運算  %%
% D1=D.';
% % net = feedforwardnet(100,'traingda');                % feedforwardnet,cascadeforwardnet,timedelaynet   %%trainscg, traingda, traingdm
% net = feedforwardnet([30 60 240 60 15],'traingda'); 
% net.trainparam.show = 50 ;
% net.trainparam.epochs = 10000 ;
% net.trainparam.goal = 0.01 ;
% net.trainParam.lr = 0.001 ;
% net.trainParam.max_fail = 100;   % Validation checks
% nnModel=train(net,C1,B1);
% y2=nnModel(D1);
% C_NN_y2=y2'  % 預測結果準確率


TotalTime = etime(clock, t0)               % 計算所耗費的總時間