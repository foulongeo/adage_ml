#!/usr/bin/env python
# coding: utf-8

# In[ ]:


col_rename_patients = {'Identifiant ADAGE' : 'id', 'DdN' : 'dob', 'Âge calculé' : 'age', 'Groupe AOD' : 'doac',
 'Article ADAGE PD' : 'TH_article', 'dose' : 'dosing', 'Nombre prélèvements' : 'nb_samples','Cmax' : 'cmax', 'Cmin' : 'cmin', 'Ddimères max' : 'max_ddim',
 'Ddimères min' : 'min_ddim', 'fib inclusion' : 'fib', 'Centre' : 'center_incl', "Date d'inclusion (jj/mm/aaaa)" : 'incl_date', 'Sexe (1 = Femme ; 0 = Homme)' : 'sex',
 'Poids(Kg)' : 'weight', 'Taille(cm)' : 'height', 'TA (mmHg)' : 'bp', 'Insuf Cardiaque' : 'heartf', 'Insuf Hepatique' : 'liverf',
 'OH' : 'alcohol', 'Mal Coronaire' : 'coronary', 'AVC' : 'stroke', 'Cancer' : 'cancer', 'Hemopathie' : 'haemopathy',
 'Demence' : 'dementia', 'Score CIRSG-total' : 'cirsg_tot', 'Score CIRSG-composite' : 'cirsg_comp', 'Type de FA (parox = 1 ; persist = 2 ; perma = 3)' : 'fa_type',
 'HTA' : 'high_bp', 'Diabete' : 'diabetes', 'Dyslipidémie' : 'dyslipidaemia', 'Tabac' : 'smoke', 'Surpoids' : 'obesity',
 'Score CHA2DS2-VASc' : 'chadsvasc_score', 'Score HAS-BLED' : 'hasbled_score', 'Score HEMORR2HAGES' : 'hemorrhages_score',
 'Nb medicaments' : 'nb_medications', 'Liste médicaments (DCI; DCI; DCI; ...)' : 'medication_list', 'Amiodarone' : 'amiodarone',
 'Verapamil' : 'verapamil', 'Quinidine' : 'quinidine', 'Clarithromycine' : 'clarithromycin', 'Aspirine' : 'aspirin',
 'Clopidogrel' : 'clopidogrel', 'Autre Antiplaquéttaire' : 'other_antiplt', 'AINS' : 'nsaid', 'Bêtabloquant' : 'bblocker',
 'IEC' : 'acei', 'ARA 2' : 'arbs', 'Statine' : 'statin', 'Creat (μmol/l)' : 'creat', 'Clairance (ml/min) Cockroft-Gault' : 'clcr_cockcroft',
 'Clairance(ml/min) MDRD' : 'clcr_mdrd', 'Clairance(ml/min) CKD-EPI' : 'clcr_ckdepi', 'CRP (mg/l)' : 'crp', 'Albumine (g/l)' : 'albumin',
 'Hémoglobine (g/dl)' : 'hb', 'Plaquettes (G/L)' : 'platelets', 'Leucocytes (G/L)' : 'leucocytes', 'ASAT (xN)' : 'asat',
 'ALAT (xN)' : 'alat', 'GGT (xN)' : 'ggt', 'PAL (xN)' : 'alp', 'Bilirrubine totale (xN)' : 'bili', 'Date debut (jj/mm/aaaa)' : 'doac_start_date',
 'SUIVI A 6 MOIS' : 'completed_f6m', '6M: Hospitalisation ?' : 'f6m_hospit', '6M: Transfusion ?' : 'f6m_transfusion',
 '6M: Hemorragie ?': 'f6m_bleed', '6M: Si Hemorragie : Type' : 'f6m_bleed_type', '6M: Si Hemorragie : Date' : 'f6m_bleed_date',
 '6M: Thrombo-Embolie ?' : 'f6m_te', '6M: Si Thrombo-embolie : Type' : 'f6m_te_type', '6M: Si Thrombo-embolie : Date' : 'f6m_te_date',
 '6M: Décès ?' : 'f6m_death', '6M: Si décès : Date' : 'f6m_death_date', '6M:  Toujours sous NACO ?' : 'f6m_still_doac',
 'SUIVI A 12 MOIS' : 'completed_f12m', '12M: Hospitalisation ?' : 'f12m_hospit', '12M: Transfusion ?' : 'f12m_transfusion',
 '12M: Hemorragie ?' : 'f12m_bleed', '12M: Si Hemorragie : Type' : 'f12m_bleed_type', '12M: Si Hemorragie : Date' : 'f12m_bleed_date',
 '12M: Thrombo-Embolie ?' : 'f12m_te', '12M: Si Thrombo-embolie : Type' : 'f12m_te_type', '12M: Si Thrombo-embolie : Date' : 'f12m_te_date',
 '12M: Décès ?' : 'f12m_death', '12M: Si décès : Date' : 'f12m_death_date', '12M:  Toujours sous NACO ?' : 'f12m_still_doac',
 'IMC' : 'bmi', 'CRP5' : 'is_crp_above_5', 'IR selon Cockcroft (0 >90; 1 >60; 2>30; 3<30)' : 'kidneyf_class', 'IR binaire +/- 50 (1 si < 50)': 'kidneyf_50',
 'Substrats de la PgP' : 'pgp_substrate_nb', 'Inhibiteurs de PgP' : 'pgp_inhib_nb', 'Tout Médicament interragissant avec pgp' : 'pgp_all_nb',
 'Au moins 1 médicament interagissantavec pgp' : 'pgp_1_all', 'Au moins 1 substrat pgp' : 'pgp_1_substrate',
 'Au moins 1 inhibiteur de pgp' : 'pgp_1_inhib', 'Substrat CYP' : 'cyp_substrate_nb', 'Inhibiteurs CYP' : 'cyp_inhib_nb',
 'Inducteurs CYP' : 'cyp_induct_nb', 'Tout Médicament interragissant avec CYP' : 'cyp_all_nb', 'Au moins 1 médicament interagissantavec CYP' : 'cyp_1_all',
 'Au moins 1 substrat CYP' : 'cyp_1_substrate', 'Au moins 1 inhibiteur CYP' : 'cyp_1_inhib', 'ISRS' : 'ssri',
 'IRSNa' : 'snra', 'ISRS+IRSNa' : 'ssri_snra', 'anticoagulant' : 'anticoagulant', 'Amlodipine' : 'amlodipine',
 'Alprazolam' : 'alprazolam', 'Atorvastatine' : 'atorvastatin', 'Bisoprolol' : 'bisoprolol', 'Citalopram' : 'citalopram',
 'Diazépam' : 'diazepam', 'Diltiazem' : 'diltiazem', 'Digoxine' : 'digoxin', 'Irbésartan' : 'irbesartan', 'Lansoprazole' : 'lansoprazole',
 'Losartan' : 'losartan', 'Mirtazapine' : 'mirtazapine', 'Oxycodone' : 'oxycodone', 'Tamsulosine' : 'tamsulosin',
 'Simvastatine' : 'simvastatin', 'Zolpidem/clone' : 'hypnotic', 'Cancer+hémopathie' : 'cancer_haemopathy', 'Pqt norm' : 'plt_norm',
 'hyperleuco' : 'hyperleuco', 'Azolés' : 'azole', 'antiarr' : 'antiarr', 'Tout anti pqt' : 'any_anti_plt',
 "Durée de prise de l'AOD (mois)" : 'doac_duration', 'PdV avant 6 mois' : 'f6m_lost', 'PdV avant 12 mois' : 'f12m_lost',
 'Hémorragie M6+M12' : 'f6_12m_bleed', 'Thrombose M6+12' : 'f6_12m_te', 'Saignement majeur 6+12' : 'f6_12m_major_bleed',
 'saignement majeur 6' : 'f6m_major_bleed', 'saignement majeur 12' : 'f12m_major_bleed', 'Identité saignement M6' : 'f6m_bleed_id',
 'Identité thrombose M6' : 'f6m_te_id', 'délais thromb' : 'te_time',  'delta saignement 6m' : 'bleed_time', 'delta décès 6m' : 'death_time',
 'GÉNÉTIQUE' : 'completed_genetics', 'ABCB1 ex21 (GG)' : 'abcb1_21', 'ABCB1 ex26 (CC)' : 'abcb1_26', 'P412Gly (CC)' : 'abcb1_12',
 'CYP2J2 (GG)' : 'cyp_2j2', 'CYP3A5 (AA)' : 'cyp_3a5', 'TGT' : 'performed_any_tga', 'FIBRINOGRAPHIE' : 'performed_fibrinography',
 'THROMBODYNAMICS TGT' : 'performed_td', 'GENESIA DRUGSCREEN' : 'performed_ds', 'GENESIA TS-TM' : 'performed_ts',
 'GENESIA TS+TM' : 'performed_tm', 'inadéquation poso ?' : 'non_valid_regimen', 'Poso conforme' : 'expected_regimen',
 'sousdosage' : 'lower_regimen', 'surdosage' : 'higher_regimen',  'CMAX Rate of clot growth (µm/min)' : 'cmax_v',
 'CMAX Lag time fib (min)': 'cmax_ltfib', 'CMAX Initial rate of clot growth (µm/min)' : 'cmax_vi', 'CMAX Stationary rate of clot growth (µm/min)' : 'cmax_vst',
 'CMAX Clot size at 30min (µm)' : 'cmax_cs', 'CMAX Clot density (a.u.)' : 'cmax_d', 'CMAX Spontaneous clotting (min)' : 'cmax_tsp',
 'CMAX LT TD' : 'cmax_lt_td', 'CMAX PH TD' : 'cmax_ph_td', 'CMAX TTP TD' : 'cmax_ttp_td', 'CMAX ETP TD' : 'cmax_etp_td',
 'CMAX Amplitude stationnaire' : 'cmax_ast', 'CMAX Rate of thromb. Propagation' : 'cmax_vt', 'CMAX LT DS' : 'cmax_lt_ds',
 'CMAX PH DS' : 'cmax_ph_ds', 'CMAX TTP DS' : 'cmax_ttp_ds', 'CMAX ETP DS' : 'cmax_etp_ds', 'CMAX VI DS' : 'cmax_vi_ds',
 'CMAX ST DS' : 'cmax_st_ds', 'CMAX LT DS Norm' : 'cmax_lt_ds_norm', 'CMAXPH DS Norm' : 'cmax_ph_ds_norm',
 'CMAX TTP DS Norm' : 'cmax_ttp_ds_norm', 'CMAX ETP DS Norm' : 'cmax_etp_ds_norm', 'CMAX VI DS Norm' : 'cmax_vi_ds_norm',
 'CMAX ST DS Norm' : 'cmax_st_ds_norm', 'CMAX LT TM' : 'cmax_lt_tm', 'CMAX PH TM' : 'cmax_ph_tm', 'CMAX TTP TM' : 'cmax_ttp_tm',
 'CMAX ETP TM' : 'cmax_etp_tm', 'CMAX VI TM' : 'cmax_vi_tm', 'CMAX ST TM' : 'cmax_st_tm', 'CMAX LT TS' : 'cmax_lt_ts',
 'CMAX PH TS' : 'cmax_ph_ts', 'CMAX TTP TS' : 'cmax_ttp_ts', 'CMAX ETP TS' : 'cmax_etp_ts', 'CMAX VI TS' : 'cmax_vi_ts',
 'CMAX SI TS' : 'cmax_st_ts', 'CMAX LT TS Norm' : 'cmax_lt_ts_norm', 'CMAX PH TS Norm' : 'cmax_ph_ts_norm', 'CMAX TTP TS Norm' : 'cmax_ttp_ts_norm',
 'CMAX ETP TS Norm' : 'cmax_etp_ts_norm', 'CMAX VS TS Norm' : 'cmax_vs_ts_norm', 'CMAX SI TS Norm' : 'cmax_st_ts_norm',
 'CMAX LT inhib' : 'cmax_lt_inhib', 'CMAX PH inhib' : 'cmax_ph_inhib', 'CMAX TTP inhib' : 'cmax_ttp_inhib', 'CMAX ETP inhib' : 'cmax_etp_inhib',
 'CMAX VI inhib' : 'cmax_vi_inhib', 'CMAX ST inhib' : 'cmax_st_inhib', 'CMIN Rate of clot growth (µm/min)' : 'cmin_v',
 'CMIN Lag time fib (min)' : 'cmin_ltfib', 'CMIN Initial rate of clot growth (µm/min)' : 'cmin_vi', 'CMIN Stationary rate of clot growth (µm/min)' : 'cmin_vst',
 'CMIN Clot size at 30min (µm)' : 'cmin_cs', 'CMIN Clot density (a.u.)' : 'cmin_d', 'CMIN Spontaneous clotting (min)' : 'cmin_tsp',
 'CMIN LT TD' : 'cmin_lt_td', 'CMIN PH TD' : 'cmin_ph_td', 'CMIN TTP TD' : 'cmin_ttp_td', 'CMIN ETP TD' : 'cmin_etp_td',
 'CMIN Amplitude stationnaire' : 'cmin_ast', 'CMIN Rate of thromb. Propagation' : 'cmin_vt', 'CMIN LT DS' : 'cmin_lt_ds',
 'CMIN PH DS' : 'cmin_ph_ds', 'CMIN TTP DS' : 'cmin_ttp_ds', 'CMIN ETP DS' : 'cmin_etp_ds', 'CMIN VI DS' : 'cmin_vi_ds',
 'CMIN ST DS' : 'cmin_st_ds', 'CMIN LT DS Norm' : 'cmin_lt_ds_norm', 'CMIN PH DS Norm' : 'cmin_ph_ds_norm',
 'CMIN TTP DS Norm' : 'cmin_ttp_ds_norm', 'CMIN ETP DS Norm' : 'cmin_etp_ds_norm', 'CMIN VI DS Norm' : 'cmin_vi_ds_norm',
 'CMIN ST DS Norm' : 'cmin_st_ds_norm', 'CMIN LT TM' : 'cmin_lt_tm', 'CMIN PH TM' : 'cmin_ph_tm', 'CMIN TTP TM' : 'cmin_ttp_tm',
 'CMIN ETP TM' : 'cmin_etp_tm', 'CMIN VI TM' : 'cmin_vi_tm', 'CMIN ST TM' : 'cmin_st_tm', 'CMIN LT TS' : 'cmin_lt_ts',
 'CMIN PH TS' : 'cmin_ph_ts', 'CMIN TTP TS' : 'cmin_ttp_ts', 'CMIN ETP TS' : 'cmin_etp_ts', 'CMIN VI TS' : 'cmin_vi_ts',
 'CMIN SI TS' : 'cmin_st_ts', 'CMIN LT TS Norm' : 'cmin_lt_ts_norm', 'CMIN PH TS Norm' : 'cmin_ph_ts_norm',
 'CMIN TTP TS Norm' : 'cmin_ttp_ts_norm', 'CMIN ETP TS Norm' : 'cmin_etp_ts_norm', 'CMIN VI TS Norm' : 'cmin_vi_ts_norm',
 'CMIN SI TS Norm' : 'cmin_st_ts_norm', 'CMIN LT inhib' : 'cmin_lt_inhib', 'CMIN PH inhib' : 'cmin_ph_inhib', 'CMIN TTP inhib': 'cmin_ttp_inhib',
 'CMIN ETP inhib': 'cmin_etp_inhib', 'CMIN VI inhib': 'cmin_vi_inhib', 'CMIN ST inhib' : 'cmin_st_inhib'    
}

col_to_delete_patients = ['NIP', 'Nom', 'Prénom', 'Article ADAGE PK', 'Article Thrombodynamics', 'PhD TGT',
 'PhD Global', 'ddi inclusion', 'DIVERS', 'Origine', "N° d'inclusion", 'Age (ans)', 'Fréq cardiaque (bpm)', 'COMORBIDITÉS',
 'Insuf Renale', 'autre 1 (texte libre)', 'autre 2 (texte libre)', 'autre 3 (texte libre)', 'autre 4 (texte libre)',
 'CARDIO-VASCULAIRE', 'MÉDICAMENTS', 'Ketoconazole', 'Itraconazole','BIOLOGIE','Fibrinogène (g/l)', 'AOD', 'Molécule', 'Posologie (mg*nb prises/j)', 'Dose totale journalière (mg)',
 'Spécialité du prescripteur ', 'Lieu excercice prescripteur', 'PARAMETRES CALCULÉS','CRP>5', 'Nombre de médic', 'Bis liste médicaments',
 'AVANCEMENT SUIVI CLINIQUE', 'Etat du suivi clinique (0 = pdv avant 6 mois, 1 = suivi à 6 mois fait, 2 = suivi à 12 mois fait)',
 'Décédaille ? (0=non ; 1 = décès avant 6 mois ; 2 = décès avant 12 mois)', 'Inclusion','thromb 6M','décès 6M', 'saigne 6M', 'Adaptation poso', 'bis date de début',
 'Quel AOD ?', 'a quelle pôsault', 'ClCR', 'Créat', 'Poids', 'CMAX FIBRINOGRAPHIE', 'CMAX THROMBODYNAMICS TGT','Le patient aurait du avoir + (2) ou moins (1) ou CI pradaxa (3)',
 'CMAX GENESIA DRUGSCREEN', 'CMAX GENESIA TS+TM', 'CMAX GENESIA TS-TM', 'CMIN FIBRINOGRAPHIE', 'CMIN THROMBODYNAMICS TGT', 'CMIN GENESIA DRUGSCREEN',
 'CMIN GENESIA TS+TM', 'CMIN GENESIA TS-TM', 'CMIN GENESIA % inhibition', 'CMAX GENESIA % inhibition']

col_to_delete_pkpd_others = ['IDENTITÉ', 'Nom', 'Prénom', 'Article ADAGE global PK', 'Article Thrombodynamics ', 'TGT PhD', 'PhD Global',
 'Delta calculé', 'ID prélèvement', 'CINÉTIQUE', 'Activité mesurée en centre', 'Anti Xa ou IIa (ng/mL)', 'Cmax', 'Cmin', 'GENESIA TS Normalisé', 'GENESIA % inhibition', 'GENESIA DRUGSCREEN Norm']

col_rename_pkpd_others = {
 'AOD' : 'doac', "Numéro d'inclusion" : 'id', 'Article ADAGE global PD' : 'TH_article', 'Date de prélèvement' : 'sampling_date',
 'Heure de prélèvement' : 'sampling_time', 'Date de dernière prise' : 'intake_date', 'Heure de dernière prise' : 'intake_time',
 'Pic ?' : 'is_cmax', 'Résiduel ?' : 'is_cmin', 'Pic/Res' : 'is_cmax_cmin', 'Sous-dosage' : 'lower_regimen', 'Surdosage' : 'higher_regimen',
 'Saignement M6' : 'f6m_bleed', 'Dose quotidienne' : 'dosing', 'DELTA Prise' : 'delta_intake_sampling', 'conc molaire (nM)' : 'molar_conc',
 'd-dimères' : 'ddim', 'Fibrinogène (g/L)' : 'fib', 'Axa totale' : 'conc', 'GENESIA TS-TM' : 'performed_ts', 'LT TS' : 'lt_ts',
 'PH TS' : 'ph_ts', 'TTP TS' : 'ttp_ts', 'ETP TS' : 'etp_ts', 'VI TS' : 'vi_ts', 'ST TS' : 'st_ts', 'LT TS Norm' : 'lt_ts_norm',
 'PH TS Norm' : 'ph_ts_norm', 'TTP TS Norm' : 'ttp_ts_norm', 'ETP TS Norm' : 'etp_ts_norm', 'VI TS Norm' : 'vi_ts_norm',
 'ST TS Norm' : 'st_ts_norm', 'GENESIA TS+TM' : 'performed_tm', 'LT TM' : 'lt_tm', 'PH TM' : 'ph_tm', 'TTP TM' : 'ttp_tm',
 'ETP TM' : 'etp_tm', 'VI TM' : 'vi_tm', 'ST TM' : 'st_tm', 'LT inhib': 'lt_inhib', 'PH inhib' : 'ph_inhib', 'TTP inhib' : 'ttp_inhib',
 'ETP inhib' : 'etp_inhib', 'VI inhib' : 'vi_inhib', 'ST inhib' : 'st_inhib', 'GENESIA DRUGSCREEN' : 'performed_ds',
 'LT DS' : 'lt_ds', 'PH DS' : 'ph_ds', 'TTP DS' : 'ttp_ds', 'ETP DS' : 'etp_ds', 'VI DS' : 'vi_ds', 'ST DS' : 'st_ds',
 'LT DS Norm' : 'lt_ds_norm', 'PH DS Norm' : 'ph_ds_norm', 'TTP DS Norm' : 'ttp_ds_norm', 'ETP DS Norm' : 'etp_ds_norm',
 'VI DS Norm' : 'vi_ds_norm', 'ST DS Norm' : 'st_ds_norm', 'THROMBODYNAMICS TGT' : 'performed_td', 'LT TD' : 'lt_td',
 'PH TD' : 'ph_td', 'TTP TD' : 'ttp_td', 'ETP TD' : 'etp_td', 'Amplitude stationnaire' : 'ast', 'Rate of thromb. Propagation' : 'vt',
 'FIBRINOGRAPHIE' : 'performed_fibrinography', 'Rate of clot growth (µm/min)' : 'v', 'Lag time (min)' : 'ltfib', 'Initial rate of clot growth (µm/min)' : 'vi',
 'Stationary rate of clot growth (µm/min)' : 'vs', 'Clot size at 30min (µm)' : 'cs', 'Clot density (a.u.)' : 'd', 'Spontaneous clotting (min)' : 'tsp'
}

