import React, { useState } from 'react';
import { ChevronLeft, ChevronRight, ShieldCheck, Network, Globe, Lock, Info, AlertTriangle, BookOpen } from 'lucide-react';

const App = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const slides = [
    {
      title: "AWS VPC(Virtual Private Cloud, 가상 프라이빗 클라우드) 개요",
      type: "intro",
      content: (
        <div className="space-y-6">
          <div className="bg-blue-50 p-6 rounded-xl border-l-4 border-blue-500">
            <h3 className="text-xl font-bold mb-2 flex items-center gap-2">
              <Network className="text-blue-600" /> VPC의 정의
            </h3>
            <p className="text-gray-700 leading-relaxed">
              VPC(Virtual Private Cloud, 가상 프라이빗 클라우드)는 AWS 클라우드 내에서 사용자 계정 전용으로 논리적으로 격리된 가상 네트워크 섹션을 할당하는 서비스입니다. 이는 온프레미스(On-premises, 자체 구축 서버 환경) 데이터 센터에서 운영하던 전통적인 네트워크를 클라우드 환경에서 가상화하여 구현한 것입니다.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="p-4 border rounded-lg bg-white shadow-sm">
              <h4 className="font-bold text-blue-700 mb-2">격리성 및 보안</h4>
              <p className="text-sm text-gray-600">다른 고객의 네트워크와 완전히 분리되어 독립적인 주소 공간과 보안 정책을 적용받습니다.</p>
            </div>
            <div className="p-4 border rounded-lg bg-white shadow-sm">
              <h4 className="font-bold text-blue-700 mb-2">높은 제어권</h4>
              <p className="text-sm text-gray-600">IP 주소 범위 선택, 서브넷 생성, 라우팅 테이블 구성 등을 사용자가 직접 설계합니다.</p>
            </div>
          </div>

          <div className="mt-4 p-4 bg-gray-100 rounded-lg text-xs text-gray-500">
            * 주석: VPC 자체 생성은 무료이지만, 데이터 전송료 및 NAT Gateway 등 부가 구성 요소는 비용이 발생할 수 있습니다.
          </div>
        </div>
      )
    },
    {
      title: "VPC 핵심 구성 요소: 주소와 서브넷",
      type: "components",
      content: (
        <div className="space-y-6">
          <section>
            <h3 className="text-lg font-bold flex items-center gap-2 mb-3">
              <Info className="text-indigo-600" /> CIDR(Classless Inter-Domain Routing, 클래스 없는 도메인 간 라우팅)
            </h3>
            <p className="text-gray-700 mb-2">VPC에서 사용할 IP 주소의 범위를 정의하는 방식입니다. 보통 <code className="bg-gray-200 px-1 rounded">10.0.0.0/16</code>와 같은 형식으로 표기합니다.</p>
          </section>

          <section>
            <h3 className="text-lg font-bold flex items-center gap-2 mb-3">
              <Network className="text-green-600" /> 서브넷(Subnet, 하위 망)
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-green-50 p-4 rounded-lg border border-green-200">
                <h4 className="font-bold text-green-800 mb-2 flex items-center gap-2">
                  <Globe size={18} /> Public Subnet(퍼블릭 서브넷)
                </h4>
                <p className="text-sm text-gray-700">인터넷 게이트웨이를 통해 인터넷과 직접 통신이 가능한 영역입니다. 외부 접근이 필요한 웹 서버 등을 배치합니다.</p>
              </div>
              <div className="bg-red-50 p-4 rounded-lg border border-red-200">
                <h4 className="font-bold text-red-800 mb-2 flex items-center gap-2">
                  <Lock size={18} /> Private Subnet(프라이빗 서브넷)
                </h4>
                <p className="text-sm text-gray-700">외부 인터넷과 직접 연결되지 않는 폐쇄된 영역입니다. 데이터베이스(Database)나 중요 로직 서버를 보호하기 위해 사용합니다.</p>
              </div>
            </div>
          </section>

          <div className="mt-4 p-4 bg-yellow-50 rounded-lg border border-yellow-200 text-sm text-yellow-800 flex gap-3">
            <AlertTriangle className="flex-shrink-0" />
            <div>
              <strong>실무 팁:</strong> 서브넷은 반드시 하나의 AZ(Availability Zone, 가용 영역) 내에 존재해야 합니다. 고가용성을 위해 여러 AZ에 서브넷을 분산 배치하는 것이 기본입니다.
            </div>
          </div>
        </div>
      )
    },
    {
      title: "VPC 연결 및 게이트웨이",
      type: "connectivity",
      content: (
        <div className="space-y-4">
          <div className="flex flex-col gap-4">
            <div className="flex items-start gap-4 p-4 border rounded-xl bg-white">
              <div className="p-2 bg-blue-100 rounded-lg text-blue-600 font-bold">IGW</div>
              <div>
                <h4 className="font-bold">IGW(Internet Gateway, 인터넷 게이트웨이)</h4>
                <p className="text-sm text-gray-600 leading-relaxed">VPC 리소스와 인터넷 간의 통신을 가능하게 하는 수평 확장형 리소스입니다. 퍼블릭 서브넷의 관문 역할을 합니다.</p>
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 border rounded-xl bg-white">
              <div className="p-2 bg-orange-100 rounded-lg text-orange-600 font-bold">RT</div>
              <div>
                <h4 className="font-bold">Route Table(라우팅 테이블, 경로 테이블)</h4>
                <p className="text-sm text-gray-600 leading-relaxed">네트워크 트래픽이 목적지 주소에 따라 어디로 전달되어야 하는지 정의한 규칙 모음입니다.</p>
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 border rounded-xl bg-orange-50 border-orange-200">
              <div className="p-2 bg-orange-600 rounded-lg text-white font-bold flex items-center">NAT <AlertTriangle size={14} className="ml-1"/></div>
              <div>
                <h4 className="font-bold text-orange-900">NAT Gateway(Network Address Translation Gateway, 네트워크 주소 변환 게이트웨이) <span className="text-red-600 text-xs">[유료 서비스]</span></h4>
                <p className="text-sm text-gray-700 leading-relaxed">프라이빗 서브넷의 인스턴스가 인터넷에 연결될 수 있도록(예: 보안 패치 다운로드) 돕는 서비스입니다. 외부에서 내부로의 직접 접속은 차단합니다.</p>
              </div>
            </div>
          </div>
          <p className="text-xs text-gray-500 mt-2 italic">* NAT Gateway는 시간당 이용료와 데이터 처리 요금이 모두 발생하므로 사용하지 않을 때는 즉시 삭제해야 합니다.</p>
        </div>
      )
    },
    {
      title: "VPC 이중 보안 체계",
      type: "security",
      content: (
        <div className="space-y-6">
          <div className="overflow-x-auto">
            <table className="w-full text-sm text-left border-collapse">
              <thead className="bg-gray-100">
                <tr>
                  <th className="p-3 border">비교 항목</th>
                  <th className="p-3 border bg-blue-50 text-blue-800">SG(Security Group, 보안 그룹)</th>
                  <th className="p-3 border bg-green-50 text-green-800">NACL(Network Access Control List)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="p-3 border font-semibold">적용 범위</td>
                  <td className="p-3 border">인스턴스(Instance) 레벨</td>
                  <td className="p-3 border">서브넷(Subnet) 레벨</td>
                </tr>
                <tr>
                  <td className="p-3 border font-semibold">상태 유지 여부</td>
                  <td className="p-3 border font-bold text-blue-600">Stateful (상태 유지)</td>
                  <td className="p-3 border font-bold text-green-600">Stateless (상태 비저장)</td>
                </tr>
                <tr>
                  <td className="p-3 border font-semibold">규칙 적용</td>
                  <td className="p-3 border">허용(Allow)만 가능</td>
                  <td className="p-3 border">허용 및 거부(Deny) 가능</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="bg-gray-50 p-4 rounded-lg border text-sm space-y-2">
            <p><strong>주석:</strong></p>
            <p>1. <strong>Stateful(상태 유지):</strong> 들어오는 트래픽이 허용되면, 나가는 트래픽은 설정과 무관하게 자동으로 허용되는 방식입니다.</p>
            <p>2. <strong>Stateless(상태 비저장):</strong> 들어오는 트래픽을 허용했더라도, 나가는 트래픽 경로를 명시적으로 허용하지 않으면 응답이 차단되는 방식입니다.</p>
          </div>
        </div>
      )
    },
    {
      title: "VPC 설계 베스트 프랙티스(Best Practices)",
      type: "summary",
      content: (
        <div className="space-y-6">
          <div className="grid grid-cols-1 gap-4">
            <div className="flex gap-4 p-4 bg-white shadow-sm border rounded-lg items-center">
              <div className="bg-blue-100 p-3 rounded-full text-blue-600"><ShieldCheck /></div>
              <div>
                <h4 className="font-bold">최소 권한 원칙 준수</h4>
                <p className="text-sm text-gray-600">보안 그룹 설정 시 필요한 포트와 IP 대역만 정밀하게 개방하십시오.</p>
              </div>
            </div>
            <div className="flex gap-4 p-4 bg-white shadow-sm border rounded-lg items-center">
              <div className="bg-green-100 p-3 rounded-full text-green-600"><Network /></div>
              <div>
                <h4 className="font-bold">고가용성 확보</h4>
                <p className="text-sm text-gray-600">최소 2개 이상의 AZ(가용 영역)에 서브넷을 구축하여 시스템의 내결함성을 확보하십시오.</p>
              </div>
            </div>
            <div className="flex gap-4 p-4 bg-white shadow-sm border rounded-lg items-center">
              <div className="bg-purple-100 p-3 rounded-full text-purple-600"><BookOpen /></div>
              <div>
                <h4 className="font-bold">미래를 고려한 IP 설계</h4>
                <p className="text-sm text-gray-600">VPC CIDR는 설정 후 변경이 불가능하므로 서비스 확장을 고려하여 넉넉히(보통 /16) 설정하십시오.</p>
              </div>
            </div>
          </div>
          
          <div className="p-6 bg-indigo-900 text-white rounded-2xl text-center">
            <p className="text-lg font-bold mb-2">VPC는 단순한 망 분리가 아닙니다.</p>
            <p className="opacity-80">클라우드 아키텍처의 보안과 가용성을 결정짓는 가장 중요한 기반 공사입니다.</p>
          </div>
        </div>
      )
    }
  ];

  const nextSlide = () => {
    if (currentSlide < slides.length - 1) setCurrentSlide(currentSlide + 1);
  };

  const prevSlide = () => {
    if (currentSlide > 0) setCurrentSlide(currentSlide - 1);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-4 md:p-8 font-sans antialiased text-slate-900">
      <div className="max-w-4xl w-full bg-white rounded-3xl shadow-2xl overflow-hidden border border-gray-100 flex flex-col h-[750px]">
        {/* Header */}
        <div className="bg-slate-900 text-white p-6 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-blue-500 rounded-lg">
              <Network size={24} />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight">AWS 인프라 전문가 과정</h1>
              <p className="text-xs text-blue-300 font-medium">AWS VPC Core Concepts</p>
            </div>
          </div>
          <div className="text-sm font-mono opacity-60">
            {currentSlide + 1} / {slides.length}
          </div>
        </div>

        {/* Progress Bar */}
        <div className="w-full h-1 bg-gray-200">
          <div 
            className="h-full bg-blue-500 transition-all duration-300 ease-out" 
            style={{ width: `${((currentSlide + 1) / slides.length) * 100}%` }}
          />
        </div>

        {/* Content Area */}
        <div className="flex-1 p-8 overflow-y-auto">
          <h2 className="text-3xl font-extrabold mb-8 text-slate-800 border-b pb-4">
            {slides[currentSlide].title}
          </h2>
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            {slides[currentSlide].content}
          </div>
        </div>

        {/* Footer Navigation */}
        <div className="p-6 bg-gray-50 border-t flex justify-between items-center">
          <button 
            onClick={prevSlide}
            disabled={currentSlide === 0}
            className={`flex items-center gap-2 px-6 py-3 rounded-full font-bold transition-all ${
              currentSlide === 0 
              ? "text-gray-300 cursor-not-allowed" 
              : "text-slate-700 hover:bg-white hover:shadow-md active:scale-95"
            }`}
          >
            <ChevronLeft size={20} /> 이전
          </button>
          
          <div className="hidden md:flex gap-2">
            {slides.map((_, idx) => (
              <div 
                key={idx}
                className={`w-2.5 h-2.5 rounded-full ${idx === currentSlide ? "bg-blue-600 w-6" : "bg-gray-300"} transition-all`}
              />
            ))}
          </div>

          <button 
            onClick={nextSlide}
            disabled={currentSlide === slides.length - 1}
            className={`flex items-center gap-2 px-8 py-3 rounded-full font-bold transition-all ${
              currentSlide === slides.length - 1 
              ? "bg-gray-200 text-gray-400 cursor-not-allowed" 
              : "bg-blue-600 text-white hover:bg-blue-700 hover:shadow-lg active:scale-95"
            }`}
          >
            {currentSlide === slides.length - 1 ? "학습 완료" : "다음"} <ChevronRight size={20} />
          </button>
        </div>
      </div>
      
      <div className="mt-8 text-center text-gray-400 text-sm">
        © 2026 VPC Curriculum Architecture. All rights reserved.
      </div>
    </div>
  );
};

export default App;
