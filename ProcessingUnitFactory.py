from ProcessingUnit import ProcessingUnit  # for processing units


class ProcessingUnitFactory(object):

    def __init__(self):
        pass

    # Builds the list of processing units detailed by the command line argument.
    # first_idx is defined as the first Processing Rate idx in sys.argv[].
    # last_idx is defined as the last Processing Rate idx in sys.argv[].
    # idx loops related to buffer size are ignored as they are already accessed via an 'idx+1' during
    # odd numbered loops.
    def build_processing_unit_list(self, sys_vector, num_of_proc_units):
        proc_unit_list = []
        first_idx = 5
        last_idx = ((num_of_proc_units) * 2) + first_idx
        for idx in range(first_idx, last_idx):
            if idx % 2 == 1:
                m_proc_rate = int(sys_vector[idx])
                m_buffer_size = int(sys_vector[idx+1])
                m_proc_unit = ProcessingUnit(m_proc_rate, m_buffer_size)
                proc_unit_list.append(m_proc_unit)
        return proc_unit_list