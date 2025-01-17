import torch


configurations = {
    1: dict(
        SEED = 1337, # random seed for reproduce results

        DATA_ROOT = './data', # the parent root where your train/val/test data are stored
        MODEL_ROOT = './model', # the root to buffer your checkpoints
        LOG_ROOT = './log', # the root to log your train/val status
        BACKBONE_RESUME_ROOT = None,#'model/Backbone_GhostNet_Epoch_9_Batch_118710_Time_2020-03-05-13-07_checkpoint.pth',#'model/Backbone_ShuffleNetV2_2.0_Epoch_19_Batch_250610_Time_2020-03-02-11-42_checkpoint.pth',
        HEAD_RESUME_ROOT = None,#'model/Head_ArcFace_Epoch_9_Batch_118710_Time_2020-03-05-13-07_checkpoint.pth',#'model/Head_ArcFace_Epoch_19_Batch_250610_Time_2020-03-02-11-42_checkpoint.pth',

        BACKBONE_NAME = 'MobileFaceNet', # support: ['ResNet_50', 'ResNet_101', 'ResNet_152', 'IR_50', 'IR_101', 'IR_152', 'IR_SE_50', 'IR_SE_101', 'IR_SE_152']
        HEAD_NAME = 'ArcFace', # support:  ['Softmax', 'ArcFace', 'CosFace', 'SphereFace', 'Am_softmax']
        LOSS_NAME = 'Focal', # support: ['Focal', 'Softmax']

        INPUT_SIZE = [112, 112], # support: [112, 112] and [224, 224]
        RGB_MEAN = [0.5, 0.5, 0.5], # for normalize inputs to [-1, 1]
        RGB_STD = [0.5, 0.5, 0.5],
        EMBEDDING_SIZE = 512, # feature dimension
        BATCH_SIZE = 128,
        DROP_LAST = True, # whether drop the last batch to ensure consistent batch_norm statistics
        LR = 0.01, # initial LR
        NUM_EPOCH = 125, # total epoch number (use the firt 1/25 epochs to warm up)
        WEIGHT_DECAY = 5e-4, # do not apply to batch_norm parameters
        MOMENTUM = 0.9,
        STAGES = [35, 65, 95], # epoch stages to decay learning rate

        DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
        MULTI_GPU = False, # flag to use multiple GPUs; if you choose to train with single GPU, you should first run "export CUDA_VISILE_DEVICES=device_id" to specify the GPU card you want to use
        GPU_ID = [0], # specify your GPU ids
        PIN_MEMORY = True,
        NUM_WORKERS = 0,
),
}
