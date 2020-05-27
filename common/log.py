#encoding=utf-8
import logging.config
import logging
import os
print(os.path.abspath('../'))

log_conf_path = 'config/logger.conf'
logging.config.fileConfig(log_conf_path)
logger = logging.getLogger()

#日志配置文件：多个logger,每个logger，指定不同的handler
#handler:设定了日志输出行的格式
#handler:以及设定写日志到文件（是否回滚）？还是到屏幕
#handler：还定了打印日志的级别。


def logDebug(message):
        # 打印debug级别的日志方法
    print('debug')
    logger.debug(message)

def logWrning(message):
    # 打印warning级别的日志方法
    logger.warning(message)

def logInfo(message):
    # 打印info级别的日志方法
    logger.info(message)

if __name__=="__main__":
    logDebug("hi")
    logWrning("gloryroad")
    logInfo("hello")