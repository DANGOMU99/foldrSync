import filecmp
import os
import time
import shutil
import logging


def sync_folders(source, replica, log_file, time_interval):
    # Checks if the replica folder exists, and if not, creates it with the provided name
    if not os.path.isdir(replica):
        logging.info('Replica folder did not exist, created with name: ' + replica + ', it will be synced with '+ source)
        os.mkdir(replica)

    # Checks if the source folder exists, and if not, creates it with the provided name
    if not os.path.isdir(source):
        logging.info('Source folder did not exist, created with name: ' + source)
        os.mkdir(source)

    logging.info('Started synchronization with parameters:\nsource_folder_name:' + source + '\nreplica_folder_name:'
                 + replica + '\nlog:' + log_file + '\ntime_interval:' + str(time_interval) + ' seconds\n')

    # Compares the folders every n seconds, n being the provided time_interval
    while True:
        try:
            compare_folders(source, replica)
            time.sleep(time_interval)
        except KeyboardInterrupt:
            print('Interrupted Synchronization')
            exit()


def compare_folders(source_f, replica_f):
    src_files = os.listdir(source_f)
    repl_files = os.listdir(replica_f)

    for file in src_files:
        source_file_path = os.path.join(source_f, file)
        replica_file_path = os.path.join(replica_f, file)

        if os.path.isdir(source_file_path):
            continue

        if file in repl_files:
            if filecmp.cmp(source_file_path, replica_file_path, False):
                log_message = file + ' is synced.'
            else:
                os.remove(replica_file_path)
                shutil.copy2(source_file_path, replica_file_path)
                log_message = file + ' has been updated.'
        else:
            shutil.copy2(source_file_path, replica_file_path)
            log_message = file + ' has been copied.'

        logging.info(log_message)
        print(log_message)

    for file in repl_files:
        if file not in src_files:
            os.remove(os.path.join(replica_f, file))
            log_message = file + ' has been deleted.'
            logging.info(log_message)
            print(log_message)

    filecmp.clear_cache()


if __name__ == '__main__':
    src = input('Please input the name for the source folder.\n')
    repl = input('Please input the name for the replica folder.\n')
    logfile = input('Please input the name for the log file.\n') + '.txt'
    interval = int(input('Please input the time interval for the synchronization.\n'))

    logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')
    sync_folders(src, repl, logfile, interval)