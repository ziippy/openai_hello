from openai import OpenAI
client = OpenAI()

def upload():
    # JSONL 파일 업로드
    response = client.files.create(
      file=open("my_training_data.jsonl", "rb"),
      purpose="fine-tune"
    )

    print("File uploaded. File Info:", response)
    # File uploaded. File Info: FileObject(id='file-JkuxKcmxbqpiLxzi9AtS9U', bytes=1694, created_at=1735477670, filename='my_training_data.jsonl', object='file', purpose='fine-tune', status='processed', status_details=None)
    #
    #
    # File uploaded. File Info: FileObject(id='file-8cfhES3s4PHGUmbtTpwjaN', bytes=2304, created_at=1735478157, filename='my_training_data.jsonl', object='file', purpose='fine-tune', status='processed', status_details=None)

def fine_tune():
    response = client.fine_tuning.jobs.create(
        training_file="file-8cfhES3s4PHGUmbtTpwjaN",
        model="gpt-4o-mini-2024-07-18"
    )
    print(response)
    # FineTuningJob(id='ftjob-a308vfcPA0tSNMeqFdkRDuX4', created_at=1735477919, error=Error(code=None, message=None, param=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(batch_size='auto', learning_rat
    # e_multiplier='auto', n_epochs='auto'), model='gpt-4o-mini-2024-07-18', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=[], seed=1141628654, status='validating_files', trained_tokens=None, t
    # raining_file='file-JkuxKcmxbqpiLxzi9AtS9U', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=None, supervised=MethodSupervised(hyperparameters=MethodSupervisedHyperparameters(batch_size='auto', learning_rate_multiplier='auto', n_epochs='auto')), type='supervised'), user_provided_suffix=None)
    #
    # FineTuningJob(id='ftjob-I3ZxS2477o4IhMPQqH2PMKto', created_at=1735478233, error=Error(code=None, message=None, param=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(batch_size='auto', learning_rat
    # e_multiplier='auto', n_epochs='auto'), model='gpt-4o-mini-2024-07-18', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=[], seed=952749579, status='validating_files', trained_tokens=None, tr
    # aining_file='file-8cfhES3s4PHGUmbtTpwjaN', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=None, supervised=MethodSupervised(hyperparameters=MethodSupervisedHyperparameters(batch_size='auto', learning_rate_multiplier='auto', n_epochs='auto')), type='supervised'), user_provided_suffix=None)

def fine_tune_list():
    # List 10 fine-tuning jobs
    lists = client.fine_tuning.jobs.list(limit=10)
    print(lists)
    # SyncCursorPage[FineTuningJob](data=[FineTuningJob(id='ftjob-I3ZxS2477o4IhMPQqH2PMKto', created_at=1735478233, error=Error(code=None, message=None, param=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparame
    # ters(batch_size=1, learning_rate_multiplier=1.8, n_epochs=10), model='gpt-4o-mini-2024-07-18', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=[], seed=952749579, status='running', trained_
    # tokens=None, training_file='file-8cfhES3s4PHGUmbtTpwjaN', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=None, supervised=MethodSupervised(hyperparameters=MethodSupervisedHyperparameters(batch_si
    # ze=1, learning_rate_multiplier=1.8, n_epochs=10)), type='supervised'), user_provided_suffix=None), FineTuningJob(id='ftjob-a308vfcPA0tSNMeqFdkRDuX4', created_at=1735477919, error=Error(code='invalid_n_examples', message='Trainin
    # g file has 7 example(s), but must have at least 10 examples', param='training_file'), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(batch_size='auto', learning_rate_multiplier='auto', n_epochs='auto'),
    #  model='gpt-4o-mini-2024-07-18', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=[], seed=1141628654, status='failed', trained_tokens=None, training_file='file-JkuxKcmxbqpiLxzi9AtS9U', vali
    # dation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=None, supervised=MethodSupervised(hyperparameters=MethodSupervisedHyperparameters(batch_size='auto', learning_rate_multiplier='auto', n_epochs='auto')),
    #  type='supervised'), user_provided_suffix=None), FineTuningJob(id='ftjob-rECaQPZd0I5N2rYDF1mhwIXT', created_at=1735477855, error=Error(code='invalid_training_file', message="The job failed due to an invalid training file. Invali
    # d file format. Input file file-JkuxKcmxbqpiLxzi9AtS9U is in the fine-tune-chat format, but the specified fine-tuning job is not using 'supervised' as the training method (provided method=dpo). ", param='training_file'), fine_tun
    # ed_model=None, finished_at=None, hyperparameters=None, model='gpt-4o-2024-08-06', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=[], seed=1579934098, status='failed', trained_tokens=None,
    # training_file='file-JkuxKcmxbqpiLxzi9AtS9U', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=MethodDpo(hyperparameters=MethodDpoHyperparameters(batch_size='auto', beta=0.1, learning_rate_multiplie
    # r='auto', n_epochs='auto')), supervised=None, type='dpo'), user_provided_suffix=None), FineTuningJob(id='ftjob-0RJpHYusexynRk7JnJIXZyrz', created_at=1735477845, error=Error(code='invalid_training_file', message="The job failed d
    # ue to an invalid training file. Invalid file format. Input file file-JkuxKcmxbqpiLxzi9AtS9U is in the fine-tune-chat format, but the specified fine-tuning job is not using 'supervised' as the training method (provided method=dpo
    # ). ", param='training_file'), fine_tuned_model=None, finished_at=None, hyperparameters=None, model='gpt-4o-2024-08-06', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=[], seed=1308670788,
    # status='failed', trained_tokens=None, training_file='file-JkuxKcmxbqpiLxzi9AtS9U', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=MethodDpo(hyperparameters=MethodDpoHyperparameters(batch_size='au
    # to', beta=0.1, learning_rate_multiplier='auto', n_epochs='auto')), supervised=None, type='dpo'), user_provided_suffix=None), FineTuningJob(id='ftjob-NlTwTTLcNJfwoeix0I65omGK', created_at=1735477783, error=Error(code='invalid_tra
    # ining_file', message="The job failed due to an invalid training file. Invalid file format. Input file file-JkuxKcmxbqpiLxzi9AtS9U is in the fine-tune-chat format, but the specified fine-tuning job is not using 'supervised' as th
    # e training method (provided method=dpo). ", param='training_file'), fine_tuned_model=None, finished_at=None, hyperparameters=None, model='gpt-4o-2024-08-06', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IG
    # R', result_files=[], seed=1188533872, status='failed', trained_tokens=None, training_file='file-JkuxKcmxbqpiLxzi9AtS9U', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=MethodDpo(hyperparameters=MethodDpoHyperparameters(batch_size='auto', beta=0.1, learning_rate_multiplier='auto', n_epochs='auto')), supervised=None, type='dpo'), user_provided_suffix=None)], object='list', has_more=False)

def fine_tune_detail():
    # Retrieve the state of a fine-tune
    r_info = client.fine_tuning.jobs.retrieve("ftjob-I3ZxS2477o4IhMPQqH2PMKto")
    print(r_info)
    # FineTuningJob(id='ftjob-I3ZxS2477o4IhMPQqH2PMKto', created_at=1735478233, error=Error(code=None, message=None, param=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(batch_size=1, learning_rate_mul
    # tiplier=1.8, n_epochs=10), model='gpt-4o-mini-2024-07-18', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=[], seed=952749579, status='running', trained_tokens=None, training_file='file-8cf
    # hES3s4PHGUmbtTpwjaN', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=None, supervised=MethodSupervised(hyperparameters=MethodSupervisedHyperparameters(batch_size=1, learning_rate_multiplier=1.8, n_epochs=10)), type='supervised'), user_provided_suffix=None)
    #
    # FineTuningJob(id='ftjob-I3ZxS2477o4IhMPQqH2PMKto', created_at=1735478233, error=Error(code=None, message=None, param=None), fine_tuned_model='ft:gpt-4o-mini-2024-07-18:personal::Ajo5kvNY', finished_at=1735480673, hyperparameters
    # =Hyperparameters(batch_size=1, learning_rate_multiplier=1.8, n_epochs=10), model='gpt-4o-mini-2024-07-18', object='fine_tuning.job', organization_id='org-hVFoG7DI3G1uEXBa06E91IGR', result_files=['file-BbWhuViwibhJz5VxXDWT7f'], s
    # eed=952749579, status='succeeded', trained_tokens=4480, training_file='file-8cfhES3s4PHGUmbtTpwjaN', validation_file=None, estimated_finish=None, integrations=[], method=Method(dpo=None, supervised=MethodSupervised(hyperparameters=MethodSupervisedHyperparameters(batch_size=1, learning_rate_multiplier=1.8, n_epochs=10)), type='supervised'), user_provided_suffix=None)

def fine_tune_check():
    # Cancel a job
    # client.fine_tuning.jobs.cancel("ftjob-abc123")
    #
    # List up to 10 events from a fine-tuning job
    # events = client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-I3ZxS2477o4IhMPQqH2PMKto", limit=10)
    # print(events)
    # SyncCursorPage[FineTuningJobEvent](data=[FineTuningJobEvent(id='ftevent-5p1KiVM1hEWQownjTMN5b88u', created_at=1735478303, level='info', message='Fine-tuning job started', object='fine_tuning.job.event', data=None, type='message'
    # ), FineTuningJobEvent(id='ftevent-6ivYbTKhXVgc5q60QwgdhrXZ', created_at=1735478299, level='info', message='Files validated, moving job to queued state', object='fine_tuning.job.event', data={}, type='message'), FineTuningJobEven
    # t(id='ftevent-5YtgsknBtZc1ZJHVKEP03FVA', created_at=1735478234, level='info', message='Validating training file: file-8cfhES3s4PHGUmbtTpwjaN', object='fine_tuning.job.event', data={}, type='message'), FineTuningJobEvent(id='ftevent-xKuUUzQHrhRGLiZ2L3gC76HD', created_at=1735478233, level='info', message='Created fine-tuning job: ftjob-I3ZxS2477o4IhMPQqH2PMKto', object='fine_tuning.job.event', data={}, type='message')], object='list', has_more=False)
    #
    # # Delete a fine-tuned model
    # client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:abc123")
    pass

if __name__ == "__main__":
    # upload()
    # fine_tune()
    # fine_tune_list()
    fine_tune_detail()