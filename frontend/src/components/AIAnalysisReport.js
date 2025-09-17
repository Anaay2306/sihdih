import React from 'react';
import { useTranslation } from 'react-i18next';

const AIAnalysisReport = ({ analysisData }) => {
  const { t } = useTranslation();

  if (!analysisData) {
    return (
      <div className="ai-analysis-report">
        <div className="no-analysis">
          <h3>{t('aiAnalysis.noAnalysisYet')}</h3>
          <p>{t('aiAnalysis.enterSymptomsPrompt')}</p>
        </div>
      </div>
    );
  }

  const getRiskLevelColor = (riskLevel) => {
    switch (riskLevel) {
      case 'critical': return '#dc3545';
      case 'high': return '#fd7e14';
      case 'medium': return '#ffc107';
      case 'low': return '#28a745';
      default: return '#6c757d';
    }
  };

  const getConfidenceText = (confidence) => {
    if (confidence >= 0.8) return t('aiAnalysis.confidenceLevels.veryHigh');
    if (confidence >= 0.6) return t('aiAnalysis.confidenceLevels.high');
    if (confidence >= 0.4) return t('aiAnalysis.confidenceLevels.moderate');
    if (confidence >= 0.2) return t('aiAnalysis.confidenceLevels.low');
    return t('aiAnalysis.confidenceLevels.veryLow');
  };

  return (
    <div className="ai-analysis-report">
      <div className="report-header">
        <h2>{t('aiAnalysis.title')}</h2>
        <p className="subtitle">{t('aiAnalysis.subtitle')}</p>
      </div>

      {/* Emergency Warning */}
      {analysisData.emergency_required && (
        <div className="emergency-warning alert alert-danger">
          <h4>{t('aiAnalysis.emergencyWarning')}</h4>
          <p>{t('aiAnalysis.emergencyMessage')}</p>
          <div className="emergency-actions">
            <button className="btn btn-danger">
              {t('aiAnalysis.actions.callEmergency')}
            </button>
          </div>
        </div>
      )}

      <div className="analysis-content">
        {/* Risk Level */}
        <div className="analysis-section">
          <h3>{t('aiAnalysis.riskLevel')}</h3>
          <div 
            className="risk-level-badge"
            style={{ 
              backgroundColor: getRiskLevelColor(analysisData.risk_level),
              color: 'white',
              padding: '8px 16px',
              borderRadius: '4px',
              display: 'inline-block'
            }}
          >
            {t(`aiAnalysis.riskLevels.${analysisData.risk_level}`)}
          </div>
        </div>

        {/* Confidence */}
        <div className="analysis-section">
          <h3>{t('aiAnalysis.confidence')}: {Math.round(analysisData.confidence * 100)}%</h3>
          <p className="confidence-explanation">
            {getConfidenceText(analysisData.confidence)}
          </p>
        </div>

        {/* Possible Conditions */}
        <div className="analysis-section">
          <h3>{t('aiAnalysis.possibleConditions')}</h3>
          <ul>
            {analysisData.possible_conditions?.map((condition, index) => (
              <li key={index}>{condition}</li>
            ))}
          </ul>
        </div>

        {/* AI Cure */}
        {analysisData.ai_cure && (
          <div className="analysis-section">
            <h3>{t('aiAnalysis.aiCure')}</h3>
            <div className="cure-content">
              <p>{analysisData.ai_cure}</p>
            </div>
          </div>
        )}

        {/* Doctor Solution */}
        {analysisData.doctor_solution && (
          <div className="analysis-section">
            <h3>{t('aiAnalysis.doctorSolution')}</h3>
            <div className="doctor-solution">
              <p>{analysisData.doctor_solution}</p>
            </div>
          </div>
        )}

        {/* Emergency Signs */}
        {analysisData.emergency_signs?.length > 0 && (
          <div className="analysis-section emergency-signs">
            <h3>{t('aiAnalysis.emergencySigns')}</h3>
            <ul className="warning-list">
              {analysisData.emergency_signs.map((sign, index) => (
                <li key={index} className="warning-item">⚠️ {sign}</li>
              ))}
            </ul>
          </div>
        )}

        {/* Complications */}
        {analysisData.complications?.length > 0 && (
          <div className="analysis-section">
            <h3>{t('aiAnalysis.complications')}</h3>
            <ul>
              {analysisData.complications.map((complication, index) => (
                <li key={index}>{complication}</li>
              ))}
            </ul>
          </div>
        )}

        {/* Prevention */}
        {analysisData.prevention && (
          <div className="analysis-section">
            <h3>{t('aiAnalysis.prevention')}</h3>
            <p>{analysisData.prevention}</p>
          </div>
        )}

        {/* Duration */}
        {analysisData.duration && (
          <div className="analysis-section">
            <h3>{t('aiAnalysis.duration')}</h3>
            <p>{analysisData.duration}</p>
          </div>
        )}

        {/* Recommendations */}
        <div className="analysis-section">
          <h3>{t('aiAnalysis.recommendations')}</h3>
          <ul>
            {analysisData.recommendations?.map((recommendation, index) => (
              <li key={index}>{recommendation}</li>
            ))}
          </ul>
        </div>

        {/* Similar Cases */}
        {analysisData.similar_cases?.length > 0 && (
          <div className="analysis-section">
            <h3>{t('aiAnalysis.similarCases')}</h3>
            <div className="similar-cases">
              {analysisData.similar_cases.map((case_item, index) => (
                <div key={index} className="case-card">
                  <h4>{case_item.diagnosis}</h4>
                  <p><strong>{t('aiAnalysis.caseDetails.patientAge')}:</strong> {case_item.patient_age}</p>
                  <p><strong>{t('aiAnalysis.caseDetails.symptoms')}:</strong> {case_item.symptoms?.join(', ')}</p>
                  <p><strong>{t('aiAnalysis.caseDetails.similarityScore')}:</strong> {Math.round(case_item.similarity_score * 100)}%</p>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* AI Insights */}
        {analysisData.ai_insights && (
          <div className="analysis-section">
            <h3>{t('aiAnalysis.aiInsights')}</h3>
            <div className="ai-insights">
              <p><strong>{t('aiAnalysis.analysisMethod')}:</strong> {analysisData.ai_insights.analysis_method}</p>
              <p><strong>{t('aiAnalysis.databaseCases')}:</strong> {analysisData.ai_insights.database_cases_analyzed}</p>
              <p><strong>{t('aiAnalysis.matchingAlgorithm')}:</strong> {analysisData.ai_insights.matching_algorithm}</p>
              <p><strong>{t('aiAnalysis.followUp')}:</strong> {analysisData.ai_insights.follow_up_timeline}</p>
            </div>
          </div>
        )}
      </div>

      {/* Action Buttons */}
      <div className="analysis-actions">
        <button className="btn btn-primary">
          {t('aiAnalysis.actions.bookConsultation')}
        </button>
        <button className="btn btn-secondary">
          {t('aiAnalysis.actions.saveReport')}
        </button>
        <button className="btn btn-outline-secondary">
          {t('aiAnalysis.actions.shareReport')}
        </button>
      </div>

      {/* Emergency Numbers */}
      <div className="emergency-numbers">
        <h4>{t('aiAnalysis.emergencyNumbers.title')}</h4>
        <div className="emergency-contacts">
          <span>{t('aiAnalysis.emergencyNumbers.ambulance')}</span>
          <span>{t('aiAnalysis.emergencyNumbers.medical')}</span>
          <span>{t('aiAnalysis.emergencyNumbers.police')}</span>
          <span>{t('aiAnalysis.emergencyNumbers.fire')}</span>
        </div>
      </div>

      {/* Disclaimer */}
      <div className="disclaimer">
        <h4>{t('aiAnalysis.disclaimer.title')}</h4>
        <p>{t('aiAnalysis.disclaimer.text')}</p>
        <p><strong>{t('aiAnalysis.disclaimer.emergency')}</strong></p>
      </div>
    </div>
  );
};

export default AIAnalysisReport;
