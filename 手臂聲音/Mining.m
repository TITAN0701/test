%  ?行SVM?性可分的二分??理
%  1、首先需要一????据train，并且已知???据的???性，在?里，?性只有??，并用1，2?表示。
%  2、通?svmtrain（只能?理2分???）函?，??行分?器的??
%  3、通?svmclassify函?，根据??后?得的模型svm_struct，?????据test?行分?
clear all;
close all;
clc;
train1=[0 0;2 4;3 3;3 4;4 2;4 4;4 3;5 3;6 2;7 1;2 9;3 8;4 6;4 7;5 6;5 8;6 6;7 4;8 4;10 10];                                              %???据?
group1=[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]'; %???据已知分?情?
                                                                            %与train?序??
test=[3 2;4 8;6 5;7 6;2 5;5 2];                                                    %???据

%??分?模型

%svmModel = svmtrain(train,group,'kernel_function','linear','showplot',true);

%分???
%classification=svmclassify(svmModel,test,'Showplot',true);
xlsFile = 'C:\Users\abc86\Desktop\手臂聲音\mfcc.xlsx';
B = xlsread(xlsFile, '工作表2', 'B1:B72')		% 讀出 'Sheet2' 的全部資料

C = xlsread(xlsFile, '工作表2', 'C1:KQ72')
D = xlsread(xlsFile, '工作表5', 'B1:KP4')
predict = zeros(4);
%SVM
%svmModel1=svmtrain(C,B,'kernel_function','linear','shoplot',true);
svmModel=svmtrain(B,C)
for i = 1:4
    % 作???，svmpredict第一????便??就可以
    predict(i) = svmpredict(0,D(i,:),svmMode);
end

%Logistic regression
E=mnrfit(C,B)
Scores = mnrval(E, D);

%Neural Network
C1=C.';
s = length(B) ;
B3 = zeros( s , 3  ) ;
for i = 1 : s 
   B3( i , B( i )  ) = 1 ;
end

B1=B3.';

D1=D.';
net = feedforwardnet(50);
net.trainparam.show = 50 ;
net.trainparam.epochs = 500 ;
net.trainparam.goal = 0.01 ;
net.trainParam.lr = 0.01 ;
nnModel=train(net,C1,B1)
y2=nnModel(D1)
y2=y2'