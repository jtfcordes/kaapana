import os
import glob
from datetime import timedelta

from kaapana.operators.PytorchExecuterBaseOperator import PytorchExecuterBaseOperator
from kaapana.operators.KaapanaBaseOperator import KaapanaBaseOperator, default_registry

class FedartedSetupCentralTestOperator(PytorchExecuterBaseOperator):

    def __init__(self,
                 dag,
                 name='federated-setup-central-test',
                 execution_timeout=timedelta(minutes=20),
                 *args, **kwargs
                 ):

        super().__init__(
            dag=dag,
            name=name,
            # cmds=["tail"],
            # arguments=["-f", "/dev/null"], 
            cmds=["/bin/bash"],
            arguments=["/executables/federated_setup_central_test/run.sh"], 
            execution_timeout=execution_timeout,
            ram_mem_mb=1000,
            ram_mem_mb_lmt=3000,
            *args, **kwargs
        )